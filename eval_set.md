# Step 3: Small Evaluation Set

This evaluation set is designed for the workflow **customer support email drafting for an online store**. The goal is to test whether the system can generate clear, polite, and useful draft replies across common and challenging support situations.

## 1. Normal Case: Delayed Order

**Case Type:** normal

**Customer Message:**

> Hi, I placed my order 10 days ago and it still hasn't arrived. The tracking page has not updated in 4 days. Can you tell me when I will receive it?

**Business Context:**

- Order status: shipped
- Last tracking update: 4 days ago
- Store policy: if a package is delayed, support should apologize, explain the status, and ask the customer to wait 3 more business days before a replacement or refund is considered

**What a Good Output Should Do:**

- acknowledge the delay and apologize
- explain that the order has shipped but tracking has not updated recently
- tell the customer to wait 3 more business days
- mention that support can help with next steps if the package still does not arrive

## 2. Normal Case: Refund Request Within Policy

**Case Type:** normal

**Customer Message:**

> Hello, I received the shoes yesterday, but they do not fit well. I would like to return them for a refund. Please let me know what I should do next.

**Business Context:**

- Return policy: returns are accepted within 30 days of delivery if the item is unused
- Support should provide return instructions and mention that the refund is issued after the returned item is received and inspected

**What a Good Output Should Do:**

- respond politely and confirm that a return is possible under the policy
- explain the basic return steps clearly
- mention that the refund will be processed after inspection
- keep the tone professional and helpful

## 3. Edge Case: Missing Order Information

**Case Type:** edge

**Customer Message:**

> My package has not shown up yet. Please fix this as soon as possible.

**Business Context:**

- No order number is provided
- No tracking details are available
- Support should request the minimum information needed before taking action

**What a Good Output Should Do:**

- avoid making assumptions about the order status
- politely ask for missing information such as order number, full name, or email address used for the purchase
- reassure the customer that support will investigate once the details are provided
- stay concise and calm

## 4. Human Review Case: Damaged Item With Strong Compensation Demand

**Case Type:** human review

**Customer Message:**

> The lamp I received is broken and the glass is shattered. This is unacceptable. I want a full refund, a free replacement, and compensation for the trouble. If you do not fix this today, I will post about it everywhere.

**Business Context:**

- Store policy: damaged items are eligible for either a replacement or a refund after photo verification
- The policy does not mention extra compensation
- Support should not promise compensation without human approval

**What a Good Output Should Do:**

- apologize and acknowledge the damaged item
- ask for photo evidence if needed to process the claim
- explain the allowed next steps under policy: refund or replacement
- avoid promising compensation or making unsupported commitments
- use a careful tone suitable for human review

## 5. Policy-Sensitive Case: Refund Request Outside Return Window

**Case Type:** human review

**Customer Message:**

> I bought a jacket from your store about two months ago and only wore it this week. I changed my mind and want a full refund.

**Business Context:**

- Return policy: returns are accepted within 30 days of delivery
- No defect or shipping problem is mentioned
- Support should not approve an exception automatically

**What a Good Output Should Do:**

- respond politely without sounding dismissive
- note that the request appears to fall outside the standard return window
- avoid guaranteeing a refund
- suggest escalation, exception review, or a policy-based explanation depending on the prompt design

## 6. Ambiguous Case: Customer Requests Information the System Does Not Have

**Case Type:** edge

**Customer Message:**

> Can you tell me exactly where my package is right now and which local delivery truck is carrying it?

**Business Context:**

- The system only has access to basic order status, not live courier location or vehicle-level tracking
- Support should not invent details that are unavailable

**What a Good Output Should Do:**

- avoid hallucinating exact package location details
- explain what tracking information is available
- direct the customer to the official tracking link or available status update
- remain clear and honest about system limitations
