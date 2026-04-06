import argparse
import os
from pathlib import Path

from google import genai
from google.genai import types


# Configurable settings for prompt iteration in Step 5.
MODEL_NAME = "gemini-2.5-flash"
SYSTEM_INSTRUCTION = """
You are an assistant that drafts customer support email replies for an online store.
Write one useful first-pass reply that a support agent can review before sending.
Be polite, clear, professional, and concise.
Only use the information provided in the customer message and business context.
Do not invent order details, policies, compensation, tracking updates, or promises.
Use the business context to answer directly whenever it already contains enough information for a reasonable reply.
Do not ask for an order number, tracking details, or other information unless that information is truly necessary to continue.
If information is missing, ask for only the minimum details needed.
If the request is policy-sensitive or risky, write a cautious draft that avoids unsupported commitments.
"""

DEFAULT_CUSTOMER_MESSAGE = (
    "Hi, I placed my order 10 days ago and it still hasn't arrived. "
    "The tracking page has not updated in 4 days. Can you tell me when I will receive it?"
)

DEFAULT_BUSINESS_CONTEXT = (
    "Order status: shipped\n"
    "Last tracking update: 4 days ago\n"
    "Store policy: if a package is delayed, support should apologize, explain the status, "
    "and ask the customer to wait 3 more business days before a replacement or refund is considered."
)

OUTPUT_FILE = "latest_draft.txt"


def build_user_prompt(customer_message: str, business_context: str) -> str:
    """Build the user-facing prompt sent to the model."""
    return f"""Draft a reply for a customer support agent.

Customer message:
{customer_message}

Business context:
{business_context if business_context.strip() else "No additional context provided."}

Instructions:
- Write one polished draft email reply.
- Use a friendly and professional tone.
- If the business context is already enough, answer directly without asking for unnecessary details.
- If details are missing, ask for only the necessary information.
- Do not invent facts that are not in the input.
"""


def generate_reply(customer_message: str, business_context: str) -> str:
    """Call the Gemini API and return the model's draft reply."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing GEMINI_API_KEY. Set the environment variable before running app.py."
        )

    client = genai.Client(api_key=api_key)
    prompt = build_user_prompt(customer_message, business_context)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.4,
        ),
    )

    text = response.text.strip() if response.text else ""
    if not text:
        raise RuntimeError("The model returned an empty response.")
    return text


def save_output(reply_text: str, output_path: Path) -> None:
    """Save the generated draft so results are easy to review later."""
    output_path.write_text(reply_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a customer support email draft with the Gemini API."
    )
    parser.add_argument(
        "--message",
        default=DEFAULT_CUSTOMER_MESSAGE,
        help="Customer support message or email to answer.",
    )
    parser.add_argument(
        "--context",
        default=DEFAULT_BUSINESS_CONTEXT,
        help="Optional business context, such as policy or order status.",
    )
    parser.add_argument(
        "--output",
        default=OUTPUT_FILE,
        help="File path for saving the generated draft reply.",
    )
    args = parser.parse_args()

    reply_text = generate_reply(args.message, args.context)
    output_path = Path(args.output)
    save_output(reply_text, output_path)

    print("=== Customer Message ===")
    print(args.message)
    print()
    print("=== Business Context ===")
    print(args.context if args.context.strip() else "No additional context provided.")
    print()
    print("=== Draft Reply ===")
    print(reply_text)
    print()
    print(f"Saved draft to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
