# ELACE 3D Labs — RAG Knowledge Base

This knowledge base is organized as modular, customer-facing source documents for a Retrieval-Augmented Generation (RAG) chatbot.

## Directory structure

- `00_governance/` — source-of-truth rules and terminology
- `01_company/` — company overview, services, FAQ
- `02_printing/` — FDM/SLA technical knowledge and design guidance
- `03_materials/` — material-selection information
- `04_products/` — product catalogue and individual products, including products shown in the 2026 brochure
- `05_orders/` — ordering, files, quotations, payment and order status
- `06_delivery/` — lead times, shipping and tracking
- `07_policies/` — returns, refunds, cancellation, warranty and replacement
- `08_services/` — custom printing, prototyping, CAD and post-processing
- `09_support/` — troubleshooting and human escalation
- `99_testing/` — RAG test questions

## Maintenance rules

1. Treat active policy documents as authoritative for customer-facing policy questions.
2. Update the relevant modular document instead of creating a duplicate document with conflicting information.
3. Increase the document `version` whenever substantive content changes.
4. Update `last_updated` whenever content changes.
5. Mark obsolete information as `deprecated` rather than leaving conflicting active versions.
6. Never invent prices, lead times, material availability, specifications, policies or capabilities.
7. If information is missing or conflicting, the chatbot should say so and recommend contacting ELACE 3D Labs rather than guessing.
8. Frequently changing operational data such as live stock, order status and tracking should ideally be supplied by an application/database integration rather than static RAG content.

## Important data-quality note

The initial knowledge base was generated from information verbally supplied by ELACE 3D Labs. Items that require later confirmation are marked `TODO` or `VERIFY`. They should not be treated as confirmed facts by a production chatbot until reviewed.

## Suggested ingestion metadata

Each document contains YAML-style metadata including:
- `document_id`
- `document_type`
- `category`
- `status`
- `version`
- `last_updated`
- `audience`
- `source`

For a production ingestion pipeline, these fields can be mapped to vector-store metadata and used for filtering/version control.

## External source used for one technical specification

The Elegoo Mars 5 Ultra build volume and Z-axis accuracy in the SLA document were checked against ELEGOO's official specifications: build volume 153.36 × 77.76 × 165 mm and Z-axis accuracy 0.02 mm. The official source also lists a 0.01–0.2 mm layer-thickness range. This external manufacturer data is used only for the printer specification; ELACE's own service claims remain subject to ELACE's operational reality.
