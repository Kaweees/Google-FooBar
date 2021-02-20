# Braille-Translation
My attempt to solve one of the Google FooBar Challenge's Level 1 problems titled "Braille Translation"

## Problem
Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station. You figure printing out Braille signs will help them, and – since you’ll be promoting efficiency at the same time – increase your chances of a promotion. Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2×3 grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda’s command can feel the bumps on the signs and “read” the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order:

`1 | 1 4`<br>
`2 | 2 5`<br>
`3 | 3 6`

So given the plain text word “code”, you get the Braille dots:

`11 10 11 10`<br>
`00 01 01 01`<br>
`00 10 00 00`

### Python Setup
1. Install Python 3.x or latest version.
2. Open cmd/termial/etc. and use the command `pip install string`.

