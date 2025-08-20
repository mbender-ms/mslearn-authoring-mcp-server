---
title: Context-sensitive help links
description: Learn how to effectively use context-sensitive help links in your documentation. Understand the differences between HelpID links and redirecting URLs, and how they enhance user experience.
ms.date: 06/29/2023
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 71544
---


# Context-sensitive help links

Links from the user interface to content in the Help system or to the web are called context-sensitive help links.  

There are two types:  

**HelpID links:** These are links coded with an API, where a HelpID in the code maps to metadata in the content management system. In some apps, the link opens in a Help panel within the host app, rather than in a browser window. Common examples of these are in the Microsoft 365 admin center, and in Microsoft 365 apps for desktop, such as the "?" button in some dialog boxes, and the Tell me more or Learn more links on some ribbon commands.  

**Redirecting URLs:** To prevent broken links and to facilitate localizing links, we use URLs that redirect. That is, instead of a URL like https://www.microsoft.com, we would use a URL like  https://go.microsoft.com/fwlink/p/?LinkId=86941. We call these FWLinks because the link IDs are managed in the FWLink database.  

**See also** [FWLink guidelines](~\link-guidelines\fwlink-guidelines\fwlink-guidelines.md "FWLink guidelines"), [Text links](https://styleguides.azurewebsites.net/Styleguide/Read?id=2869&topicid=71542 "Text links")  

