# Just Letters
Misc (60 points, 205 solves)

## Challenge 

Hope you’ve learned the [alphabet](https://esolangs.org/wiki/AlphaBeta)!

```
nc 54.159.113.26 19600
```

Author: derekthesnake

## Solution

This is an esolang problem. We are given documentation for this language called AlphaBeta. After connecting to the challenge, we see that the flag is at the start of memory, presumably at address 0.

I read through the documentation for a bit and decided not to write a loop to print the flag out just for the sake of time. I quickly came up with this sequence of letters:

```
YGCL
```

`Y` sets the memory pointer to 0, `G` sets register 1 to the memory at the memory pointer, `C` sets register 3 to the value of register 1, and then `L` prints the character to the screen. This will print the first character `a` to the screen. By adding `S` letters, we can shift the memory pointer down and print the second character to the screen. With a quick Python script, I generated a string that was long enough to print the whole flag.

```python
>>> print "YGCL" + "SGCL"*40
YGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCLSGCL
```

## Flag

```
actf{esolangs_sure_are_fun!}
```