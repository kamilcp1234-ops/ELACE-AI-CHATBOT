---
document_id: testing-expected-behaviour
document_type: evaluation
category: testing
status: active
version: 1.0
last_updated: 2026-09-15
audience: internal
source: ELACE 3D Labs initial knowledge capture
---

# RAG Evaluation Expectations

## Correct retrieval examples

- Company questions → `01_company/`
- FDM questions → `02_printing/fdm_printing.md`
- SLA questions → `02_printing/sla_printing.md`
- Material questions → `03_materials/`
- Product questions → `04_products/`
- Ordering questions → `05_orders/`
- Delivery questions → `06_delivery/`
- Policy questions → `07_policies/`
- Service questions → `08_services/`
- Troubleshooting/escalation → `09_support/`

## Grounding requirement

The chatbot should answer from retrieved knowledge and should not invent unsupported numerical specifications.

## Missing-data behavior

For unsupported questions, the chatbot should clearly state that the information is not confirmed and direct the customer to ELACE.

## High-risk examples

The chatbot must not invent:
- exact engineering strength,
- guaranteed dimensional accuracy,
- warranty coverage,
- refund amounts,
- delivery guarantees,
- stock,
- order status,
- tracking,
- payment methods,
- unsupported printer capabilities.
