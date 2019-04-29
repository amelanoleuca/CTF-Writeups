# Control You
Web (20 points, 1237 solves)

## Challenge 

Only those who give us the flag are exempt from [our control](https://controlyou.2019.chall.actf.co/).

Author: kmh11

## Hint

Your browser executes code when you're viewing a web page. Is it possible to see that code?

## Solution

After opening the website, we see some nice color schemes and animations. First we can check the source code by pressing Ctrl+U ("Control You"). This shows that when you click the button it compares the flag to a constant string.

## Flag

```
actf{control_u_so_we_can't_control_you}
```
