---
title: Know terms to use and terms to avoid - Responsible AI Style Guide
description: Learn the preferred terminology for discussing AI systems and avoid common pitfalls. This guide clarifies terms like "responsible AI" and "AI development life cycle," while advising against ambiguous or misleading language.
ms.date: 11/12/2024
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 60620
---


# Know terms to use and terms to avoid

**Use**

- **Use the term _responsible AI_** instead of referring to ethics or ethical AI. A [human-centered approach](~\responsible-ai-style-guide\a-z-word-list\h\human-centered-ai.md), the goal of responsible AI is to create trustworthy AI systems that benefit people while mitigating harms through research-driven best practices.

  **Note:**

  - **Do not use the terms _responsible AI system(s)_** or _responsible AI compliant_ because these terms mistakenly imply there is a once-and-done checklist for ensuring an AI system is a responsible product or service. Instead, considerations for responsible AI are ongoing throughout the entire [AI development and deployment life cycle](~\responsible-ai-style-guide\a-z-word-list\a\ai-development-and-deployment-life-cycle.md) of a system.
  - **Use lowercase _r_** for _responsible AI_, except when occurring as part of a proper noun, such as the Responsible AI Toolbox or the Responsible AI Standard.

- **Use the terms _machine learning (ML) model_ and _AI system_ correctly; they are not interchangeable.** Clarify whether a product is an ML model or an AI system: ML models are components within AI systems and typically involve data, code, and model outputs. An AI system, in addition to its ML models, has other sociotechnical components, such as a user interface.

- **Use _AI development and deployment life cycle_ instead of _ML pipeline_** to refer to stages of an AI system's existence. (Note, _ML pipeline_ is a term limited to workflows within machine-learning tasks and that does not encompass the [sociotechnical](~\responsible-ai-style-guide\a-z-word-list\s\sociotechnical.md) aspects of AI systems [e.g., see [Azure Machine Learning](/azure/machine-learning/concept-ml-pipelines?msclkid=b9903046cd8d11ec8bf39e55133fdb1e)]).

**Avoid**

- **Avoid using _bias, AI bias,_ or _algorithmic bias,_** which are often used as catchphrases for fairness issues, [fairness-related harms](~\responsible-ai-style-guide\a-z-word-list\f\fairness-related-harms.md) and their causes, and more. Instead, use the complete term statistical bias or societal bias when referring to these specific phenomena. Don’t use the word _bias_ on its own. When the intention is to communicate about societal bias, consider naming specifics, such as racism, sexism, ageism, transphobia, and so on. (See the [section on Fairness in AI systems](/fairness/fairness-in-ai.md) for more.)

- **Avoid referring to AI as a race or competition** to be won. Instead, communicate the primary goal of [responsible AI](~\responsible-ai-style-guide\a-z-word-list\r\responsible-ai.md) is to create trustworthy AI systems that benefit people while mitigating harms through research-driven, human-centered best practices.

- **Avoid using the ambiguous term _artificial general intelligence_** in general, so as to not add to confusion about the capabilities and limitations of AI systems. (See [Don't overclaim or misrepresent what AI can do](~\responsible-ai-style-guide\top-tips\dont-overclaim-or-misrepresent-what-ai-can-do.md) and [Set expectations that failures are inherent in AI systems](~\responsible-ai-style-guide\top-tips\set-expectations-that-failures-are-inherent-in-ai-systemsthey-will-happen.md).)

- **Avoid hyperbole, such as the term _magic,_** when describing AI systems or their processes, output, or user experience. (See [AI hype](~\responsible-ai-style-guide\a-z-word-list\a\ai-hype.md).)

**Terms quick reference**

| **Use this**                                                                 | **Not this**                                                                 |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| responsible AI*<br><em>*Use lowercase r for responsible AI, except when occurring in a proper noun, such as the Responsible AI Toolbox or the Responsible AI Standard.)</em> | ethical AI, ethics*<br><em>* Avoid using these terms (except when they occur in the name of a group or organization). Instead, use [responsible AI](~\responsible-ai-style-guide\a-z-word-list\r\responsible-ai.md), which denotes the practices and way of thinking that help ensure AI technologies accomplish intended benefits while mitigating harms.</em> |
|                                                                              | responsible AI compliant, responsible AI systems*<br><em>* Avoid these terms because they mistakenly imply there is a once-and-done checklist for ensuring an AI system is a responsible product or service; instead, considerations for responsible AI are ongoing throughout the entire [AI development and deployment life cycle](~\responsible-ai-style-guide\a-z-word-list\a\ai-development-and-deployment-life-cycle.md) of a system.</em> |
| AI development and deployment life cycle                                     | ML pipeline*<br><em>*A term limited to workflows within machine-learning tasks and that does not encompass the sociotechnical aspects of AI systems</em> |
| societal bias, statistical bias*<br><em>*Avoid using the term _bias_ on its own; use the terms _societal bias_ or _statistical bias_ when talking about these specific phenomena. [See more about bias](~\responsible-ai-style-guide\fairness\top-tips\know-fairness-terms-to-use-and-terms-to-avoid.md).</em> | bias, AI bias, algorithmic bias                                               |