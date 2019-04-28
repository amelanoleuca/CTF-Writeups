# Blank Paper
Misc (30 points, 660 solves)

## Challenge 

Someone scrubbed defund's [paper](https://files.actf.co/26e1d969c6a7c21d973a64a67f74ea2695ee5b8743cd8f20d9ccde665bbfd368/blank_paper.pdf) too hard, and a few of the bytes fell off. 

Author: defund

## Solution

We are given a PDF file called "blank_paper.pdf". It does not open in any PDF reader, so it is likely missing some parts.

Opening the file in a hex editor, we can see that the file does not contain the proper PDF header. We can easily fix this by adding the correct header.

```
%PDF-1.5
```

Now the file opens in a PDF reader, and the flag is near the top. 

## Flag

```
actf{knot_very_interesting}
```