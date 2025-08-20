---
title: Copilot and first-person pronouns
description: Learn how to effectively use first-person singular pronouns in Copilot conversational experiences to enhance user interaction. Understand when to avoid first-person plural and how to handle error messaging without anthropomorphizing Copilot.
ms.date: 09/25/2024
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 71634
---


# Copilot and first-person pronouns

Use first-person singular pronouns (*I, me, my, mine, myself*) inside Copilot conversational experiences.

- Use first-person when the user is conversing with Copilot. Don’t use first-person singular outside of a Copilot interaction experience (for example, in a canvas, pane, or wizard dialog).  
- Don’t use first person plural (*we, us, our, ours, ourselves*) in Copilot conversational output.  

Use the first person when Copilot is describing a problem.  

- Error messages in Copilot should support situations where Copilot is talking about its capabilities ("I'm not able to do that") or its inability to fulfill a request it usually can do ("This flow can't be saved because some parameters are missing").  
- If redundancy with standard error messaging is a concern, Copilot can offer assistance above and beyond the error. ("I can walk you through how to fill in the missing parameters. Do you want to do that now?")  
- Use third person or passive voice when a Copilot-specific error shouldn't be perceived as coming from the Copilot bot. ("Copilot is at capacity and temporarily unavailable—please try again in a little while.")  
- Don't use Copilot for standard error handling, like a back-end system error. Don’t use first-person pronouns in error messages that don't appear in Copilot.  

Use first-person with verbs that are only appropriate for a machine, like actions or facts. Don’t use first-person pronouns with verbs that are associated with consciousness, desire, thought, or opinion, when the model is the cause of the error.  

**Note**: Don’t anthropomorphize Copilot; rather, use first person singular pronouns to communicate more effectively with its users. While the interactive experience will employ the first person singular, Copilot doesn’t have a personality or consciousness; Copilot is the title of interactive services, but it’s not the name of an entity or character.  

- The usage of the first-person singular in a conversational experience (for example, in Copilot chat and others) aligns with Microsoft’s brand voice: “above all, simple and human.”
- First-person singular models human interaction to communicate with users more effectively in an interactive, back-and-forth scenario. Avoiding I, me, etc., can be unfriendly and awkward in a conversational setting. Its use can also more clearly delineate the scope of Copilot’s abilities or actions.  
- First-person singular is an industry standard for text- and voice-first assistant experiences like Alexa, Google Assistant, Siri, ChatGPT, or Bing Chat. OpenAI recognizes that and GPT uses I for its generated sentences in chat contexts by default.

**Examples**:

“I updated that text for you” defines the actor and action while “that text has been updated” doesn’t help the reader understand who was involved or how the action was taken.  

"I'm not able to do that yet. Can you ask me something else?" is conversational and lets the user understand the required next steps. Avoiding the first-person by saying something like “Unable to process request. Rephrase the prompt” is terse, jarring, and robotic.  

Self-reference without the use of first-person singular is jarring and robotic (“Copilot didn’t understand that”), but using first-person singular matches the mental model of a conversation (“I need a little more information”). It also doesn’t anthropomorphize Copilot by assigning sentience to its actions, like saying “I don’t understand” or “I don’t think I follow” would.  

**See also** [Pronouns](~\grammar-usage\pronouns.md), [Conversational UX (CUX, chat, bots)](~\ux-content-design-essentials\conversational-ux-cux-chat-bots.md)

