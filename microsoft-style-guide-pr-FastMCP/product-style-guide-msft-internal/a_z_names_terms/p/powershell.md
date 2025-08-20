---
title: PowerShell
description: Learn how to refer to PowerShell in your content.
ms.date: 11/04/2024
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 56808
---


# PowerShell

Use PowerShell to describe a scripting language and an interactive shell. References to PowerShell differ depending on the platform: PowerShell, Windows PowerShell, PowerShell modules, Azure PowerShell. Note internal capitalization on all variants.

**PowerShell:** The cross-platform version of PowerShell that's built on .NET (rather than the full .NET Framework). One word, note internal capitalization.

**Windows PowerShell:** The version of PowerShell in Windows, which requires the full .NET Framework.

**Guidelines**

First mention: Windows PowerShell

Subsequent mentions: PowerShell, unless the use case requires Windows PowerShell:

- In PowerShell, the Invoke-WebRequest cmdlet returns BasicHtmlWebResponseObject
- In Windows PowerShell, the Invoke-WebRequest cmdlet returns HtmlWebResponseObject

**PowerShell modules:** Add-ons that provide PowerShell cmdlets that manage specific products or services.

**Guidelines**

Use the proper name of the module. Example: Azure Active Directory PowerShell

Never refer to the module as *PowerShell*

**Azure PowerShell:** The collection of PowerShell modules designed for Azure.

**Guidelines**

First mention: Azure PowerShell

Subsequent mentions: Azure PowerShell (never just *PowerShell*)

Use the more specific name when referring to a specific version:

- Az PowerShell: The currently supported collection of modules for use with Azure
- AzureRM PowerShell: The earlier collection of modules that use the Azure Resource Manager model for managing Azure resources (deprecated and no longer supported after February 29, 2024)
- Azure Service Management PowerShell: The earliest collection of modules is for managing legacy Azure resources that use Service Management APIs.
- Azure Stack PowerShell: A collection of PowerShell modules used to manage Azure Stack environments. These modules are used together with other Azure PowerShell modules.

**Azure PowerShell-related modules**

Modules not included in the Azure PowerShell but are used to manage Azure resources.

**Guidelines**

First and subsequent mentions should always be the same.

- Azure Active Directory PowerShell
- AIP PowerShell
- Azure Deployment Manager PowerShell
- Azure Elastic DB Jobs PowerShell
- Azure Service Fabric PowerShell

**Other PowerShell modules**

Other Microsoft products and services publish PowerShell modules designed to manage those offerings.

**Guidelines**

First and subsequent mentions: Refer to the collective name or the specific module name: “Windows management modules” (collectively) or the Hyper-V PowerShell module (specifically).

