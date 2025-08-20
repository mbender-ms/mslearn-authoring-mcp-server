---
title: update domain
description: Learn how to refer to "update domain" in your content.
ms.date: 04/17/2023
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 28084
---


# update domain

A grouping of role instances in a cloud service that allows in-place updates to occur without affecting service availability. Azure updates a cloud service one update domain at a time. It stops the instances running within one of the update domains, updates the instances, starts them again, and then moves to the next update domain. In this way, at least one update domain stays running while another one gets updated.

**Guidelines**

Use instead of *upgrade domain*. 