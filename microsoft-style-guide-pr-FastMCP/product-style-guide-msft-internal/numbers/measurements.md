---
title: Measurements
description: Learn how to correctly format measurements in documentation, including percentages, currency, and data sizes. Follow guidelines for using numerals, abbreviations, and hyphens to ensure clarity and consistency.
ms.date: 04/17/2023
ms.topic: contributor-guide
ms.service: microsoft-product-style-guide
ms.custom:
  - TopicID 56452
---


# Measurements

In this context, measurements include percentage, currency, screen resolution, distance, dimensions, and so on, but generally not days, weeks, or other units of time. Bits and bytes are also considered units of measure. 

As a rule, outside the UI, don’t abbreviate units of measure in text. An exception is kilobytes (KB), megabytes (MB), gigabytes (GB), and terabytes (TB), which can be abbreviated when used with numbers. In the UI and other places where space is limited, you can use abbreviations as long as your audience will understand what you mean. 

Use numerals for all measurements, even if the number is less than 10. This is true whether the measurement is spelled out, abbreviated, or replaced by a symbol.

**Our style**  
5 percent   
Azure Cache for Redis will be available in the 250-MB and 1-GB sizes.  
two years

**Not our style**  
five percent   
Azure Cache for Redis will be available in the 250-MB and one-GB sizes.    
2 years

When you’re referencing two or more quantities, repeat the unit of measure.

**Our style**    
1 TB to 50 TB per month

**Not our style**  
1 to 50 TB per month

Use a hyphen between the number and the unit of measure if you’re using the measurement as an adjective. Otherwise, there should be a space between the number and the abbreviation.

**Our style**  
Prepare a 3.5-inch SATA HDD storage device.    
500-TB capacity limit   
A block blob can be up to 200 GB in size.

**Not our style**    
Prepare a 3.5 inch SATA HDD storage device.    
500 TB capacity limit   
A block blob can be up to 200-GB in size.

To designate screen resolution, use numerals without commas. Don’t spell out *by*. Instead, use the multiplication sign (×). Insert a space on either side of the × symbol.

**Our style**  
1280 × 1024

**Not our style**  
1280x1024

If it’s necessary to line-break measurements in places where space is limited—such as on a part/tile in the UI or within a table—keep the number and the unit of measurement together. If you’re representing a ratio, keep the operator together with the measurement.

**Our style**    
23 MB/ day

**Not our style**  
23 MB /day