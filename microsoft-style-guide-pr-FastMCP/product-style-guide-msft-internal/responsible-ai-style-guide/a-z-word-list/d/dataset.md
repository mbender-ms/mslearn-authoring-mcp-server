---
title: dataset - Responsible AI Style Guide
description: Learn how to refer to "dataset" in your content.
ms.date: 11/13/2024
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 63216
---


# dataset

“Every machine learning model is trained and evaluated using data, quite often in the form of static _datasets_. The characteristics of these datasets fundamentally influence a model’s behavior: a model is unlikely to perform well in the wild if its deployment context does not match its training or evaluation datasets, or if these datasets reflect unwanted societal biases” ([Source: Datasheets for datasets](https://arxiv.org/pdf/1803.09010.pdf)).

Be sure to communicate clearly about the composition of training datasets because their composition impacts what we can say about a machine learning model’s capabilities and its limitations. Avoid making vague statements about datasets, such as saying the model was trained on “human communication” or “coding practices.” Instead, be specific about [demographic groups](~\responsible-ai-style-guide\fairness\demographics-language\demographics-language-how-to-talk-about-groups-of-people.md) and other data represented in a dataset.

See more about [documenting datasets](https://www.microsoft.com/research/uploads/prod/2022/07/aether-datadoc-082522.pdf).