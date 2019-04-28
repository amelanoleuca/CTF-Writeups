# The Mueller Report
Misc (20 points, 706 solves)

## Challenge 

The redacted version of the Mueller report was finally released this week! There's some pretty funny stuff in there, but maybe [the report](https://mega.nz/#!SsMDmAhT!MjplSc7lCqUQFrZC5EL_t7f2fdoDDNwrZhfTgTAcG7s) has more beneath the surface.

Author: Sirlan

## Hint

You won't be able to use Ctrl+F to find this Russian secret, try some command line functions related to strings and searches instead.

## Solution

We are given a PDF file called "full-mueller-report.pdf". I first tried opening it and doing a search for "actf" but found nothing.

Next I tried `strings` and `grep`ing for "actf"

```
$ strings full-mueller-report.pdf | grep actf
actf{no0o0o0_col1l1l1luuuusiioooon}
```

## Flag

```
actf{no0o0o0_col1l1l1luuuusiioooon}
```