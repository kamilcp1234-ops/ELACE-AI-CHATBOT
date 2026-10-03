---
document_id: design-for-3d-printing
document_type: technical-guide
category: 3d-printing
status: active
version: 1.0
last_updated: 2026-09-15
audience: customer
source: ELACE 3D Labs initial knowledge capture
---

# Design for 3D Printing

## General principle

A model should be designed for the selected printing process, material, orientation and intended use.

## Customer-supplied models

ELACE can work with customer-supplied 3D models. The model should be printable and geometrically valid.

ELACE can attempt model repair where practical, but repair is not guaranteed.

## Orientation

Part orientation affects:
- support requirements,
- surface quality,
- print time,
- dimensional behavior,
- strength,
- visible layer lines.

For functional parts, the orientation should be selected with expected loading and layer-direction behavior in mind.

## Large models

Models larger than the printer's build volume can be split into sections. ELACE can print sections and use joints/assembly methods where appropriate.

## Tolerances

A stated typical FDM tolerance of approximately ±0.2 mm is available as a planning reference. Actual results depend on geometry, machine, material and settings.

For mating parts, customers should communicate required clearances and fit requirements before printing.

## Material selection

Material choice should be based on:
- mechanical loading,
- temperature exposure,
- flexibility,
- environmental exposure,
- appearance,
- post-processing requirements.

## Recommendation

For a quotation, provide the model and explain the intended application. ELACE can then advise on a suitable printing process and material.
