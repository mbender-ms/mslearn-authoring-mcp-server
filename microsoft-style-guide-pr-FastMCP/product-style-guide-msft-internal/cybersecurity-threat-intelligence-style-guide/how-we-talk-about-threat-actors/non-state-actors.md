---
title: Non-state actors
description: Explore the terminology and classifications for non-state threat actors in Microsoft's writing style guide. Understand the distinctions between criminal, private-sector offensive, and authorized offensive actors, and learn how to reference them consistently in documentation.
ms.date: 10/30/2023
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 63505
---


# Non-state actors

The breadth of threat actors tracked by Microsoft has expanded beyond the realm of state-linked actors and we must strive to have the same consistency and clarity of terminology in place to refer to them. There are three main types of actors in this bucket: criminal, private sector offensive actors (PSOA), and authorized offensive actors (AOA). These primary types may be further divided into subtypes.

#### Criminal threat actors

| **Topic** | **Example** | **Explanation** |
| --- | --- | --- |
| **Criminal** | “Criminal actor” | Actors operating within the cybercriminal ecosystem use a variety of operational structures, typically working toward financial gain. A subset of criminal actors – hacktivists – work with an aim of social change, but due to frequent use of defacement techniques still fall under the criminal grouping of actors. |
| **Financially motivated** | “Financially motivated actor” | Use for actors who compromise victims for financial gain without the use of ransomware or extortion. This includes actors using banking trojans or compromising networks to use machines for crypto mining. |
| **Access broker** | “Access broker actor” | Use for actors who compromise networks in order to sell that access to other actors for follow-on objectives. |
| **Ransomware** | “Ransomware actor” | Use for actors who develop and operate ransomware for their own objectives. |
| **Ransomware-as-a-service (RaaS) operator** | “RaaS operator actor” | Use for actors who develop and maintain tools used in ransomware operations. |
| **Ransomware-as-a-service (RaaS) affiliate** | “RaaS affiliate actor” | Use for actors who run the ransomware operation using tools from a RaaS operator and access from an access broker. |
| **Phishing** | “Phishing actor” | Use for actors who operate phishing campaigns to solicit personal information or legitimate credentials. |
| **Hacktivist** | “Hacktivist actor” | Use for actors operating to further the goals of the activism cause on whose behalf they are operating. This may or may not be officially sanctioned by that cause. |

#### Private-sector offensive actors (PSOA)

| **Topic** | **Example** | **Explanation** |
| --- | --- | --- |
| **Private-sector offensive actor (PSOA)** | “Private-sector offensive actor (PSOA)” (on first use) “PSOA” (subsequent use) | Private-sector offensive actor (PSOA), intrusion-as-a-service, access-as-a-service, and surveillance-for-hire are similar terms used to describe this growing sector. PSOAs are private companies that manufacture and sell cyberweapons in hacking-as-a-service packages, often to government agencies around the world, to hack into their targets’ computers, phones, network infrastructure, and other devices. Two common models for this type of actor are access-as-a-service and hack-for-hire. In access-as-a-service, the actor sells full end-to-end hacking tools that can be used by the purchaser in operations, with the PSOA not involved in any targeting or running of the operation. In hack-for-hire, detailed information is provided by the purchaser to the actor who then runs the targeted operations. |
| **Cyber mercenary** | “Cyber mercenary” | Use for companies or individuals who develop, sell, and support offensive cyber capabilities that enable their clients - often governments - to access the networks, computers, phones, or internet-connected devices or their targets in ways that violate human rights and undermine democratic principles. This is a subset of the broader PSOA term. |
| **Exploit broker** | “Exploit broker actor” | The middle layer between the user of an exploit and the developer of an exploit. This is a subset of the broader PSOA term. |
| **Vulnerability researcher** | “Vulnerability researcher” | Use for actors, both individual and organizations, that perform vulnerability research looking for novel vulnerabilities that could be used in offensive operations. It can be difficult to discern whether a vulnerability researcher is operating exclusively for the public good or for malicious purposes. This is a subset of the broader PSOA term. |
| **Capability developer** | “Capability developer” | Use for actors who find and develop capabilities, including, but not limited to exploits, but do not deploy them against targets themselves. This is a subset of the broader PSOA term. |

#### Authorized offensive actors (AOA)

| **Topic** | **Example** | **Explanation** |
| --- | --- | --- |
| **Authorized offensive actor (AOA)** | “Authorized offensive actor (AOA)” (on first use) “AOA” (subsequent use) | Use as an umbrella term to cover red teams, pen testing companies, and any other authorized actor performing offensive techniques against a knowing “victim”. The distinction from PSOA is that AOAs are known to be authorized by the organization against which they are acting or selling services/tools to. |
| **Red team** | “Red team actor” | Use for actors (often an in-house team) using offensive techniques that mimic a malicious threat actor against the organization’s network to evaluate security posture. This is a subset of the broader AOA term. |
| **Pen tester or penetration testing company** | “Penetration tester” “Penetration testing company” | Use for an individual or company that performs penetration testing or sells penetration testing tools to individuals or organizations interested in hardening their networks. When using this term, we must be careful to look for use of publicly available pen test tools by malicious actors and reclassify the actor accordingly. This is a subset of the broader AOA term. |