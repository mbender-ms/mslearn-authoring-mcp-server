---
title: FWLink guidelines
description: Learn how to effectively use FWLinks to manage redirectable URLs in your content, ensuring links remain functional and up-to-date. Discover best practices for creating, maintaining, and using FWLinks across different scenarios.
ms.date: 06/29/2023
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 48223
---


# FWLink guidelines

A FWLink (or "forward link") is a redirectable URL that can be used in our products and content to prevent broken or stale links. The target of a FWLink can be updated whenever necessary, with no changes to the code that uses the FWLink.

## Creating FWLinks

Create FWLinks at [https://aka.ms/fwlink](https://aka.ms/fwlink).

(The companion **aka.ms** tool can be used to create a vanity URL, but aka.ms links aren't localized, so they are suitable only for English links.)

- Each person is responsible for creating and maintaining their FWLinks.
- Use an appropriate security group (such as—for Office support content—**ossfwlinks**) as the group owner for your FWLink. This group includes the appropriate localization contacts and the members of the Office content team. By doing this, the correct folks will still be notified if an older FWLink changes or breaks even if the individual owner is no longer available.

## Using FWLinks

- Always use the https protocol with FWLinks.
- To improve discoverability, add the **/p** option to an FWLink, like this: _https://go.microsoft.com/fwlink/p/?LinkId=86941_

Use the information in the following table to help decide whether to use an FWLink in your content.

| Scenario | Use FWLink? | Details |
| --- | --- | --- |
| Link to a support article that lives on the same site | No | Don't use FWLinks.<br/><br/> Do not use a FWLink to link between two topics on support.microsoft.com or to link between two topics on docs.microsoft.com. |
| Link to a support article that lives on a different Microsoft site | Yes | Use FWLinks. <br/><br/>Example: Use an FWLink to link from a topic on support.microsoft.com to a topic on docs.microsoft.com. |
| Link to any external resources (non-Microsoft, third parties). | Yes | The FWLink team confirmed a policy that restricted some teams from creating FWLinks to third-party sites no longer exists. |
| Linking to other platforms, such as community sites, wikis, etc. | Recommended | Recommended, but there’s no requirement to use FWLinks when you link to content in other platforms such as community sites. Follow any existing guidelines for that platform. These FWLink guidelines apply only to DxStudio users. |
| Link from product UI to a support article | It's allowed | In Office desktop products, a Help API is the preferred method for linking to a support topic, but FWLinks are used for other cases. |