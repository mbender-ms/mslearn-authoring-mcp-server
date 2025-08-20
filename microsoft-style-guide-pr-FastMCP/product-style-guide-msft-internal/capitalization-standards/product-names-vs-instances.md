---
title: Product names vs. instances
description: Learn how to distinguish between product names and instances in documentation. 
ms.date: 04/17/2023
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 44732
---


# Product names vs. instances

Is it a product or service name—or is it an [instance](https://styleguides.azurewebsites.net/Styleguide/Read?id=2696&topicid=29134) (something created using that product or service)?

If it's an instance, lowercase all words. Use title-style capitalization for product and service names only.  

**Our style**  
Create an IoT hub and connect it to your Azure IoT services.  
Use App Service to build web apps, mobile apps, and API apps.

**Not our style**  
Create an IoT Hub and connect it to your Azure IoT services.  
Use App Service to build Web Apps, Mobile Apps, and API Apps.  

When instances are capitalized, it signals that this is the product or service itself, rather than something created using that product or service. And that makes our offerings and content hard to understand.

Localization relies on this convention. In general, localizers don't translate brand names, product names, and trademarks, but they do translate other text, such as the names of instances, category names, and technical terms. They use the capitalization of the English source text as a cue. If a name is capitalized in English, it must be a brand, product, or trademark name and therefore doesn't get translated.

Here’s an excerpt from an email exchange about whether _elastic database_ was a name or an instance. The decision was that it was an instance and therefore should be lowercase.

_If it is referring to technical term, source English will be in lower case, ex: "elastic database". Then for ja-JP, we will translate it in Katakana "エラスティック データベース"._  

_If it is referring to Azure service, source English will be in cap, "**E**lastic **D**atabase". Then for ja-JP, we will keep it in English "Elastic Database"._

