---
title: error messages (self-serve how-to guidance)
description: Learn how to craft effective error messages that enhance user experience by providing clear, concise, and actionable guidance. Discover best practices for tone, word choice, and structure to help users resolve issues efficiently.
ms.date: 02/16/2024
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 45345
---


# error messages (self-serve how-to guidance)

Error messages are alerts that inform customers of a problem that’s occurred. The best error message is the one that never shows up. But errors happen even in the best products, which is why error messages are an important component of the user experience.

A good error message should be simple, clear, consistent, and helpful. It unblocks a customer by telling them what went wrong and how to fix it, providing only critical information and nothing more.

![Error message example](~/media/1676562116.png)

## Formatting and context

Error messages should be clearly visible and should use timing and placement to make it easier to resolve the error.

When a problem occurs, try to preserve as much of your customer’s work in progress as possible.

## How to write error messages

Error messages should be specific and easy to understand so the customer can resolve the issue and be on their way.

### Formula

In general, follow this formula when writing error messages:

[What went wrong] + [What caused it, if relevant] + [How to fix it]

### Message bar and text field error messages

In general, use the formula:

[What went wrong] + [What caused it, if relevant] + [How to fix it]

![Message bar example](~/media/1355889357.png)

When space is limited, such as in text field error messages, focus on the solution.

![Text field error example](~/media/1616372238.png)

### Error messages in dialog boxes

Error messages that appear in dialog boxes follow this formula:

Title: [What went wrong]  
Body content: [Why, if relevant] + [How to fix it]  
Button label: [Clear action]

![Dialog box example](~/media/2002058569.png)

## Content

Be explicit about what happened, and tell the customer how to fix the problem or move forward:

- Be brief—one or two sentences at most. An em dash (—) or sentence fragment can be a useful way to connect the problem to the cause and the solution in a few words.  
  **Example**  
  Can't find that data. Please try again later.

- Provide just enough information to guide the customer to the solution.  
  **Example**  
  There's a problem with that password. Check to see if **Caps lock** is on.

- Sometimes, it makes sense to state the solution or action first. If space is an issue, focus on the solution.  
  **Example**  
  Enter a valid phone number.

- When you can’t specify what caused an error, it’s OK to be vague, but offer a clear solution.  
  **Example**  
  Something went wrong—try saving again in a few minutes.

## Tone and word choice

When customers are experiencing a problem, tone is even more critical:

- Be crisp and clear to unblock them efficiently.
- Stay positive, and don’t blame the customer.
- Don’t attempt to inject personality, humor, or whimsy. This can be perceived as flippant or dismissive of the issue. It also might not localize well.
- Don’t use technical language or industry jargon.
- Use *sorry* for critical errors that are our fault. But don't apologize for problems that are outside the product, such as a broken link or waiting for a network connection to be found.
- It’s OK to use *please* when you’re asking the customer to go above and beyond to resolve a problem.

Consider leading with these words and phrases:

- “There's a problem with …”
- “Can't find …”
- “Can't load …”
- “That file didn’t …”

Avoid these words and phrases:

- “There has been an error” or “An error has occurred”
- “Error,” “Failed,” “Denied,” or “Invalid”
- “Contact your admin” …  
  (Suggest this action only if you include a link so the customer can email their admin.)
- "Hmmm ..." or "Oops ..." or "Whoops ..."
- Developer error codes like “WDGeneralNetworkError Error 500”  
  (If you need to include a code, hide it under a “Get support code” text link.)

How to talk about errors and error messages:

- Use the word *problem* instead of *error, issue,* or *technical problem.*
- Refer to the error message as a *message* and not an *error* or *error message.*

## Examples

**Our style**  
There's not enough space to download this file. Free up space by deleting other files.

**Not our style**  
Download failed! Maximum capacity reached.

**Our style**  
You’ll need permission to access this file. Request access

**Not our style**  
Error code 4150: Access denied.  
You’re not authorized to sign in using your current credentials.  
Oops! This file couldn’t be opened because it looks like you don’t have access under your sign-in credentials. Contact your admin to access this file.

**Our style**  
Can't find any results for “sherpie.” Try a different search term.

**Not our style**  
Invalid search

**Our style**  
Please try again. Your password needs to contain both lowercase and uppercase characters and a special character.

**Not our style**  
Request error. Password was not validated. Invalid password, min characters groups of three not fulfilled (error code: 400)

**See also** [oops](~\a_z_names_terms\o\oops.md)

