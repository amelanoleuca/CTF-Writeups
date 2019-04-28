# I Like It
Rev (40 points, 609 solves)

## Challenge 

Now I like dollars, I like diamonds, I like ints, I like strings. Make Cardi [like it](https://files.actf.co/ced231db51437ed22dd7b244042135184436148b97cd16236bf0bc12f6139d5e/i_like_it) please.

```
/problems/2019/i_like_it
```

Author: Sirlan

## Hint

Pop open a dissassembler or decompiler and check out the comparisons.

## Solution

We are given an executable file. Using `file`, we find that it is an unstripped 64-bit Linux ELF. 

```
$ file i_like_it 
i_like_it: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=5b91e9b31dffd010d9f32b21580ac3675db92a62, not stripped
```

When we run the program, it asks us for a string. Entering in some random text outputs "Cardi don't like that." So, I tried `strings`.

```
$ strings i_like_it
...
I like the string that I'm thinking of: 
okrrrrrrr
Cardi don't like that.
I said I like it like that!
I like two integers that I'm thinking of (space separated): 
%d %d
Flag: actf{%s_%d_%d}
...
```

I went ahead and tried "okrrrrrrr" and it was correct. Then it asked for two integers, which we can't get from `strings`. Opening it up in peda, we see some functions. 

```
gdb-peda$ info fun
All defined functions:

Non-debugging symbols:
0x00000000004005d8  _init
0x0000000000400610  puts@plt
0x0000000000400620  strlen@plt
0x0000000000400630  __stack_chk_fail@plt
0x0000000000400640  printf@plt
0x0000000000400650  __libc_start_main@plt
0x0000000000400660  fgets@plt
0x0000000000400670  strcmp@plt
0x0000000000400680  __isoc99_sscanf@plt
0x0000000000400690  exit@plt
0x00000000004006b0  _start
0x00000000004006e0  deregister_tm_clones
0x0000000000400720  register_tm_clones
0x0000000000400760  __do_global_dtors_aux
0x0000000000400780  frame_dummy
0x00000000004007a6  main
0x00000000004008f0  __libc_csu_init
0x0000000000400960  __libc_csu_fini
0x0000000000400964  _fini

```

A `disas main` shows that the program gets some input and does some comparisons. We can set a breakpoint at `main` and step through the program. Lets call the first number `a` and the second number `b`. When we get the part where it asks for two numbers, we see that it puts `a` in `edx` and `b` in `eax`.

```
0x400869 <main+195>:	call   0x400680 <__isoc99_sscanf@plt>
0x40086e <main+200>:	mov    edx,DWORD PTR [rbp-0x38]
0x400871 <main+203>:	mov    eax,DWORD PTR [rbp-0x34]
```

Then, it will add a + b and compare that to 0x88 (136). If it is not equal, then the program will jump to the end of the program and end. 

```
0x400874 <main+206>:	add    eax,edx
0x400876 <main+208>:	cmp    eax,0x88
0x40087b <main+213>:	jne    0x400897 <main+241>
```

This gives us our first rule. `a + b = 136`. 

Skipping past the jump (since our two numbers aren't correct yet) with `br *0x40087d` and `jump *0x40087d`, we see that the program again puts `a` in `edx` and `b` in `eax`. Then, it will multiply a * b and compare that to `0xec7` (3783). Again, if it is not equal, then the program will jump to the end of the program and end. 

```
0x40087d <main+215>:	mov    edx,DWORD PTR [rbp-0x38]
0x400880 <main+218>:	mov    eax,DWORD PTR [rbp-0x34]
0x400883 <main+221>:	imul   eax,edx
0x400886 <main+224>:	cmp    eax,0xec7
0x40088b <main+229>:	jne    0x400897 <main+241>
```

This gives us our second rule. `a * b = 3783`. Combining this with our first rule, we can use basic algebra to solve. First rewrite `a + b = 136` as `b = 136 - a`, and substitute it into the second rule to get `a * (136 - a) = 3783`. Distributing `a` and subtracting 3783, we get the quadratic `-a^2 + 136a - 3783 = 0`. Using any method (I like to complete the square when the linear coefficient is even), we get the solutions a = 39 or a = 97. 

Using the first rule again, we find that the numbers are either (a, b) = (39, 97) or (97, 39). So which one is correct?

Skipping pas the jump again, we see that the program again puts `a` in `edx` and `b` in `eax`. This time it will compare edx and eax right away, and will jump to the correct part of the program if a is less than b. 

```
0x40088d <main+231>:	mov    edx,DWORD PTR [rbp-0x38]
0x400890 <main+234>:	mov    eax,DWORD PTR [rbp-0x34]
0x400893 <main+237>:	cmp    edx,eax
0x400895 <main+239>:	jl     0x4008ab <main+261>
```

Therefore, our numbers are (a, b) = (39, 97). After exiting out of peda we can run the program normally with these numbers. 

```
$ ./i_like_it 
I like the string that I'm thinking of: 
okrrrrrrr
I said I like it like that!
I like two integers that I'm thinking of (space separated): 
39 97
I said I like it like that!
Flag: actf{okrrrrrrr_39_97}
```

## Flag

```
actf{okrrrrrrr_39_97}
```