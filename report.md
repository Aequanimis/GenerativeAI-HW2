# Week 2 Report: Build and Evaluate a Simple GenAI Workflow

## Business Use Case

For this assignment, I selected the workflow of **customer support email drafting for an online store**. In this workflow, a customer support agent receives a customer message, along with optional business context such as order status, store policy, or handling guidelines. The system then produces a polite and helpful draft reply that the agent can review before sending.

This is a useful workflow to automate or partially automate because customer support involves a large amount of repeated written communication. Many requests follow common patterns, such as delayed orders, refund requests, damaged items, or incomplete customer information. A simple LLM-based drafting tool can save time, improve consistency, and reduce effort on routine responses while still keeping a human in the loop for review.

## Model Choice

I used **Google AI Studio / Gemini API** for the prototype. This was a practical choice because it was also the recommended default in the assignment instructions, and it provides a straightforward way to build a small Python prototype with a real LLM API call.

The model I tested in the final prototype was **`gemini-2.5-flash`**. I chose this model because it fit the assignment well: it was easy to access from Python, fast enough for a simple coursework prototype, and strong enough to generate fluent customer support drafts from short text inputs and business context.

## Baseline vs. Final Design

The baseline design used the initial system instruction from `prompts.md`. That version told the model to be polite, concise, professional, and to avoid inventing unsupported details. It also said to ask for missing information when necessary. This baseline was enough to produce a generally reasonable customer support draft, so it worked as a starting point for the prototype.

However, the delayed-order test case revealed an important weakness. In that case, the customer message and business context already included enough information to draft a useful first-pass reply: the order had shipped, tracking had not updated in four days, and the policy said the customer should wait three more business days before a replacement or refund would be considered. Even with that context, the baseline output still asked the customer for an order number. This was unnecessary and made the reply less useful.

In response, I revised the prompt twice. Revision 1 added clearer guidance that the model should not ask for extra details if the provided business context already contained enough information to answer. Revision 2 made the instruction more specific by emphasizing that the system should write **one useful first-pass reply** and should not ask for an order number, tracking details, or other information unless that information was truly necessary. The final version also stated the human-review boundary more clearly by framing the output as a draft for a support agent to review rather than a fully autonomous final response.

Compared with the baseline, the final design gives the model clearer guidance about when it should answer directly and when it should ask follow-up questions. This makes the prompt better aligned with the real business goal of drafting routine support replies efficiently. At the same time, I tried to keep the final instruction simple enough for a small student project. The main tradeoff is that the final prompt is a little more prescriptive than the baseline, which may make it slightly less flexible in unusual situations, but for this workflow that tradeoff is reasonable.

## Limitations and Human Review

This prototype still has clear limitations and should be treated as a drafting assistant, not a fully autonomous customer support system. Some cases remain better suited for human review, especially policy-sensitive requests, ambiguous customer questions, and situations where business context is missing or incomplete. For example, requests involving exceptions to return policy, compensation demands, or unclear tracking situations may require a human agent to interpret policy and make a decision.

There is also a risk that the model may produce replies that are too generic or too cautious if the prompt is not specific enough, or if the available business context is limited. Because of this, human review is still important before any reply is sent to a customer. In this workflow, the value of the system is in producing a useful first draft quickly, not in replacing the support agent's judgment.

## Deployment Recommendation

I would recommend this workflow for **limited deployment with human review**. In practice, it could be useful in a support setting where agents handle a high volume of similar written requests and want help drafting replies more quickly. It would be especially helpful for routine issues such as delayed orders, standard returns, and basic product or account questions.

I would not recommend fully autonomous deployment based on this prototype alone. A safer and more realistic use case is to deploy it as an internal drafting assistant, where the model generates a reply and a human agent checks the result before sending it. Under those conditions, this workflow appears practical and valuable: it can reduce writing effort and improve consistency while keeping final responsibility with a human reviewer.
