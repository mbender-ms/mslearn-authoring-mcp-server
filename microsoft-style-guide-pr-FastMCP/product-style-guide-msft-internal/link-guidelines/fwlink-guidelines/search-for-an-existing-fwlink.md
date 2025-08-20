---
title: Search for an existing FWLink
description: Ensure an FWLink doesn't already exist before creating a new one. Learn how to search for existing FWLinks using the redirection tool with advanced filters.
ms.date: 10/10/2022
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 48224
---


# Search for an existing FWLink

Before you create a new FWLink, check to make sure that one doesn’t already exist for the URL you want to use.

1. Copy the URL you want to search for.
2. In the [redirection tool](https://redirectiontool.trafficmanager.net/am/redirection/home?options=host:go.microsoft.com), select *Advanced Filters**.
3. Specify a **Field Name**, such as **Target URL**.
4. Specify an **Operator**, such as **Contains**.
5. Specify a **Value**, such as the GUID of the target you are looking for.
6. Select **Apply Filters**. 

The results shown to you will only include links owned by you or security groups you are a member of.

For a given result, you can see all its properties by selecting the checkbox to the left of the **Link ID** column.