## Step 2: Choose a Business Workflow and Define the Task

For this assignment, I chose the workflow of **customer support email drafting for an online store**.

The main user of this system is a **customer support agent** who needs to reply to customer messages quickly and professionally. In many small businesses, support agents spend a lot of time reading customer emails and writing responses about common issues such as delayed orders, refund requests, damaged items, and account questions.

The input to the system is:
- a customer message or email
- optional business context, such as store policy, order status, or response style guidelines

The output of the system is:
- a clear, polite, and helpful draft reply that the support agent can review and send
- if needed, the reply can also include next steps, a short apology, or a request for missing information

This task is valuable to automate or partially automate because customer support involves a large amount of repeated written communication. Drafting replies takes time, even when the issues are common. An LLM-based system can help agents respond faster, maintain a consistent tone, and reduce effort on routine messages while still allowing a human to review the final response before sending it. This makes the workflow practical for a simple prototype and suitable for evaluation with multiple test cases.

## Why This Is a Strong Choice

This workflow is a strong choice for the rest of the assignment because it is realistic, easy to explain, and well suited to a simple Python prototype with at least one LLM API call. The inputs and outputs are both plain text, so implementation is straightforward. It is also easy to create at least five test cases with different customer situations and evaluate the system based on tone, helpfulness, completeness, and accuracy.
