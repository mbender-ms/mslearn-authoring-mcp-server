---
title: Outcome vs intent
description: Learn how to differentiate between outcome and intent in cyber threat intelligence. Understand the importance of analyzing actions, outcomes, and motives in intrusion analysis to enhance forecasts and recommendations.
ms.date: 10/30/2023
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 63539
---


# Outcome vs intent

### Differentiating outcome versus intent

Within intelligence, we often analyze the actions of parties to gain a greater understanding of that party. Within cyber threat intelligence, this most often occurs in intrusion analysis. When conducting intrusion analysis, it is critical to differentiate what occurs, what was intended to occur, and why the actor wanted the outcome to occur. This should be done for every actor involved in an intrusion, in the case where there are multiple actors. In general, Microsoft Intelligence should be stating observed outcomes/impacts and aggregating/assessing motives only if it benefits a proposed forecast or recommendation.  

**Outcome –** This is the result of a particular intrusion. MITRE ATT&CK defines this as “Impact” ([Impact, Tactic TA0040 - Enterprise | MITRE ATT&CK®](https://attack.mitre.org/tactics/TA0040/)). This is objective and is modeled at the intrusion level.

**Motive/Intent –** This is the purpose for conducting a particular intrusion. Motive often requires analyst assessment (unless you have first-hand access to the actor). Motive also does not always match the outcomes accomplished, though it is fair to assess with a confidence level whether an actor accomplished their objective or fulfilled their intent.