---
title: input endpoint
description: Learn how to refer to "input endpoint" in your content.
ms.date: 11/01/2024
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 27979
---


# input endpoint

The IP and port on which a role instance receives inbound traffic.

Each type of role has restrictions on the number and type of input endpoints that can be defined. A web role can have no more than one HTTP endpoint and one HTTPS endpoint. A worker role can have no more than five HTTP, HTTPS, or TCP endpoints, in any combination. A VM role can have only one HTTP, HTTPS, or TCP endpoint.  

