# Paper Bin
Misc (40 points, 372 solves)

## Challenge 

defund accidentally deleted all of his math papers! Help recover them from his computer's [raw data](https://files.actf.co/ac4e8f7e16fb244613ffe42741046f98839e477e7a511d583dcc1bb291486029/paper_bin.dat).

Author: defund

## Hint

File carving

## Solution

We are given a data file called "paper_bin.dat". The problem description and hint suggested that the file is made up of several smaller files. 

Using `binwalk`, we can see that the file is made up of some PDF files and many Zlib streams. PDF files commonly contain Zlib streams so the Zlib streams are not useful to us. Include only PDF in `binwalk` and we can see how many PDF documents the file is made of.

```
$ binwalk --include 'pdf document' paper_bin.dat

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------222           0xDE            PDF document, version: "1.4"
352478        0x560DE         PDF document, version: "1.4"
708830        0xAD0DE         PDF document, version: "1.4"
1081566       0x1080DE        PDF document, version: "1.4"
1446110       0x1610DE        PDF document, version: "1.4"
1790174       0x1B50DE        PDF document, version: "1.4"
2171102       0x2120DE        PDF document, version: "1.4"
2531550       0x26A0DE        PDF document, version: "1.4"
2932958       0x2CC0DE        PDF document, version: "1.4"
3301598       0x3260DE        PDF document, version: "1.4"
3629278       0x3760DE        PDF document, version: "1.4"
4051166       0x3DD0DE        PDF document, version: "1.4"
4411614       0x4350DE        PDF document, version: "1.4"
4739294       0x4850DE        PDF document, version: "1.4"
5066974       0x4D50DE        PDF document, version: "1.4"
5415134       0x52A0DE        PDF document, version: "1.4"
5751006       0x57C0DE        PDF document, version: "1.4"
6082782       0x5CD0DE        PDF document, version: "1.5"
6385886       0x6170DE        PDF document, version: "1.4"
6770910       0x6750DE        PDF document, version: "1.4"
```

There appear to be many PDF 1.4 documents, but there is one PDF 1.5 document that stands out. Extract that part of the file and open it in a PDF viewer, which shows the flag. 

## Flag

```
actf{proof by triviality}
```