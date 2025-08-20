---
title: Assessments and analysis
description: Learn how to effectively convey confidence in assessments and analysis by understanding the factors that influence confidence levels. Explore how data quality, evidence bias, and alternative explanations impact the classification of confidence as high, moderate, or low.
ms.date: 10/30/2023
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 63534
---


# Assessments and analysis

### Conveying confidence - assessments and analysis

Generally, analysts’ confidence in an assessment or judgement may be based on the logic and evidentiary base that underpin it, including the quantity and quality of source material, and/or their understanding of the topic.

**Low confidence** generally means that the information’s credibility and/or plausibility is questionable, or that the information is too fragmented or poorly corroborated to make solid analytic inferences, or that we have significant concerns or problems with the sources. Alternatively, the analyst could have low confidence because their analytic judgement is based on several assumptions.

**Moderate confidence** generally means that the information is credibly sourced and plausible but not of sufficient quality or not corroborated sufficiently to warrant a higher level of confidence. Alternatively, the analyst could have moderate confidence because their analytic judgement is based on a few assumptions.

**High confidence** generally indicates that our judgments are based on high-quality information, and/or multiple, corroborated sources and/or that the nature of the issue makes it possible to render a solid judgment. A “high confidence” judgment is not a fact or a certainty, however, and such judgments still carry a risk of being wrong.

To avoid confusion, products that express an analyst's confidence in an assessment or judgment using a confidence level (e.g., "high confidence") should try to avoid using a confidence level and a degree of likelihood, which refers to an event or development, in the same sentence.

**Example:** We assess that Mint Sandstorm probably conducted this attack. Although this attack does not use either of Mint Sandstorm's previously observed custom implants, we have moderate confidence in our attribution based on how this attack matches our observations of Mint Sandstorm's initial access and persistence tradecraft and how the targeted entities match current Tehran objectives.

## Factors affecting assessment confidence

When assessing confidence, analysts must approach their classification at a high level within a structured framework. Microsoft Threat Intelligence teams and organizations use the following factors to help determine the confidence of an assessment.

- **Quality of data source –** Data has natural biases and risks associated with its use, and while observations are generally factual, they are often imperfect (i.e., we see a file for the first time on actor machine but that isn’t *actually* the first time it was seen in the world). When analyzing confidence of an assessment, we must consider all possible biases present in the data sources involved.
- **Compounding evidence bias –** When building upon multiple assumptions or assessments, resulting confidence might be lower.
- **Corroborating diverse sourcing –** Observing evidence for an assessment across multiple data sources of different types helps to support the final assessment. Diversity of data sources in evidence helps to eliminate potential risk of bias and broadly helps to compound towards a higher confidence assessment.
- **Contradictory information –** There will be times when two pieces of evidence are contradictory. The existence of contradictory information should not preclude an assessment but might alter its confidence.
- **Alternative explanations –** Plausible alternative hypotheses, or lack thereof, influence the likelihood of an assessment being accurate. Alternative and competing hypotheses should be explored and considered as part of your structured analysis.

| Confidence | Description |
|------------|-------------|
| **High**   | - Data quality is high with little bias. <br> - Stacked evidence generally aligns toward the same outcome with similarly high confidence. <br> - Multiple sources of multiple types align. <br> - There is little to no contradictory evidence. <br> - There are few or no alternative explanations. |
| **moderate** | - Data quality is moderate with some biases present that may lower confidence. <br> - Stacked evidence generally aligns toward the same outcome but might vary in confidence. <br> - Multiple sources align (not diverse). <br> - There is little contradictory evidence. <br> - There are few alternative explanations, or the explanations are unlikely. |
| **Low**    | - Data quality is low-moderate with some biases present that may lower confidence. <br> - Stacked evidence varies in alignment and varies in confidence. <br> - Evidence may be single-sourced. <br> - Some contradictory evidence may exist. <br> - There are alternative explanations. |