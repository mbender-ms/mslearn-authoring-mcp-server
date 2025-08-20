---
title: Tooltip guidelines
description: Learn how to effectively use tooltips in UI design to enhance user experience. Discover best practices for writing concise, informative tooltips that add value without redundancy.
ms.date: 09/27/2023
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 42478
---


# Tooltip guidelines

Good tooltips briefly describe unlabeled controls or provide a bit of additional info for labeled controls, when this is useful. They can also help customers navigate the UI by offering additional—not redundant—information about control labels, icons, and links.

**Tooltips should be used sparingly** Tooltips can be an interruption to the customer, so don't include one that simply repeats a label or states the obvious. A tooltip should always add valuable information. Tooltips should never be more than two short sentences. (And if it's one fragment or sentence, don't use end punctuation such as a period.)

**Don’t just repeat the label** UI labels are read by screen readers, so a tooltip that only repeats the label name isn't helpful.

If a label doesn't meet any of the below descriptions, it doesn't need a tooltip.

Punctuation for tooltips:

- Headings don't get end punctuation.
- If the descriptive text is a complete sentence or more than one sentence, include end punctuation.

| UI  element | Include a tooltip written like this |
|-------------|-------------------------------------|
| **Icon**<br>When a control or UI element is unlabeled | Use  a simple, descriptive noun phrase. For example: <br>Highlighting pen  |
| **Disabled control** that can use explanation | Provide a brief description of the state in which the control will be enabled, e.g., “This feature is available for line charts.” |
| **UI label** that needs some explanation | - *Briefly* describe what you can do with this UI element. <br>- Use the imperative verb form. For example, "Find text in this file" (not "Finds text in this file").<br>- Don't include end punctuation unless there is at least one complete sentence. |
| **Truncated label** or the label is likely to truncate in some languages | - Provide the untruncated label in the tooltip.<br>- Optional: On another line, provide a clarifying description, but only if needed.<br>- Don't provide a tooltip if the untruncated info is provided elsewhere on the page or flow.  |
| **Keyboard shortcut** is available | - Optional: Provide the keyboard shortcut in parentheses  following the descriptive phrase, e.g. "Find text in this file  (Ctrl+F)"<br>- Avoid adding a tooltip only to show a keyboard shortcut. |

**See also** Windows developer guidance on tooltips:  
[https://docs.microsoft.com/windows/uwp/controls-and-patterns/tooltips](https://docs.microsoft.com/windows/uwp/controls-and-patterns/tooltips)

