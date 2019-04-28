# One Bite
Rev (60 points, 523 solves)

## Challenge 

Whenever I have friends over, I love to brag about things that I can eat in a single bite. Can you give [this program](https://files.actf.co/697526f731d6484c6fc1066070b722e3a833bef6c3280fcbae1004083460e887/one_bite) a tasty flag that fits the bill?

```
/problems/2019/one_bite
```

Author: Sirlan

## Hint

What else can be done with a single bite?

## Solution

We are given an executable file. Using `file`, we find that it is an unstripped 64-bit Linux ELF. 

```
$ file one_bite
one_bite: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=1378c7ef8cdf59c2cbe4d84274295b2567a09e91, not stripped
```

When we run the program, it asks us for a string. Entering in some random text outputs "That didn't taste so good :(" This time, `strings` was not useful.

Opening it up in peda, we see some functions.

```
gdb-peda$ info fun
All defined functions:

Non-debugging symbols:
0x0000000000400510  _init
0x0000000000400540  puts@plt
0x0000000000400550  strlen@plt
0x0000000000400560  __stack_chk_fail@plt
0x0000000000400570  __libc_start_main@plt
0x0000000000400580  fgets@plt
0x0000000000400590  strcmp@plt
0x00000000004005b0  _start
0x00000000004005e0  deregister_tm_clones
0x0000000000400620  register_tm_clones
0x0000000000400660  __do_global_dtors_aux
0x0000000000400680  frame_dummy
0x00000000004006a6  main
0x0000000000400780  __libc_csu_init
0x00000000004007f0  __libc_csu_fini
0x00000000004007f4  _fini
```

A `disas main` shows that the program gets some input and does some comparisons. We can set a breakpoint at `main` and step through the program. The first thing we see after the call to `fgets` is some sort of loop. Our string is at `rbp-0x40`. 

```
0x00000000004006e7 <+65>:	mov    DWORD PTR [rbp-0x4c],0x0
0x00000000004006ee <+72>:	jmp    0x40070c <main+102>
0x00000000004006f0 <+74>:	mov    eax,DWORD PTR [rbp-0x4c]
0x00000000004006f3 <+77>:	cdqe   
0x00000000004006f5 <+79>:	movzx  eax,BYTE PTR [rbp+rax*1-0x40]
0x00000000004006fa <+84>:	xor    eax,0x3c
0x00000000004006fd <+87>:	mov    edx,eax
0x00000000004006ff <+89>:	mov    eax,DWORD PTR [rbp-0x4c]
0x0000000000400702 <+92>:	cdqe   
0x0000000000400704 <+94>:	mov    BYTE PTR [rbp+rax*1-0x40],dl
0x0000000000400708 <+98>:	add    DWORD PTR [rbp-0x4c],0x1
0x000000000040070c <+102>:	mov    eax,DWORD PTR [rbp-0x4c]
0x000000000040070f <+105>:	movsxd rbx,eax
0x0000000000400712 <+108>:	lea    rax,[rbp-0x40]
0x0000000000400716 <+112>:	mov    rdi,rax
0x0000000000400719 <+115>:	call   0x400550 <strlen@plt>
0x000000000040071e <+120>:	cmp    rbx,rax
0x0000000000400721 <+123>:	jb     0x4006f0 <main+74>
```

Firstly, it uses the DWORD at `rbp-0x4c` as a counter, initially st to 0. Then, from `0x40070c`, it will move that counter to `eax`, move `eax` to `rbx`. Then it will move our string at `rbp-0x40` to `rax` and call `strlen`. If the length of our string is less than the counter, we jump back into our loop at `0x4006f0`. 

From there, we move the counter into eax, then move the character at the counter in our string into `eax` (`movzx  eax,BYTE PTR [rbp+rax*1-0x40]`). Then, it will `xor` this character with 0x3c andmove it back into the string (`mov    BYTE PTR [rbp+rax*1-0x40],dl`). Lastly, it adds 1 to the counter and continues with the check above. 

Basically, this will xor each character of the string with 0x3c. After all this is done, it will compare the string to a string stored at `0x400820`. 

```
0x0000000000400723 <+125>:	mov    QWORD PTR [rbp-0x48],0x400820
0x000000000040072b <+133>:	mov    rdx,QWORD PTR [rbp-0x48]
0x000000000040072f <+137>:	lea    rax,[rbp-0x40]
0x0000000000400733 <+141>:	mov    rsi,rdx
0x0000000000400736 <+144>:	mov    rdi,rax
0x0000000000400739 <+147>:	call   0x400590 <strcmp@plt>
```

We can find this string either from our debugger or using `objdump`.

```
$ objdump -s -j .rodata one_bite 

one_bite:     file format elf64-x86-64

Contents of section .rodata:
 400800 01000200 00000000 47697665 206d6520  ........Give me 
 400810 6120666c 61672074 6f206561 743a2000  a flag to eat: .
 400820 5d5f485a 47556348 54555257 63555163  ]_HZGUcHTURWcUQc
 400830 5b535552 5b634853 635e5963 4f555f57  [SUR[cHSc^YcOU_W
 400840 41005975 6d2c2074 68617420 77617320  A.Yum, that was 
 400850 61207461 73747920 666c6167 2e005468  a tasty flag..Th
 400860 61742064 69646e27 74207461 73746520  at didn't taste 
 400870 736f2067 6f6f6420 3a2800             so good :(.
```

Starting at `0x400820` and reading until the `00` byte, the string is "]_HZGUcHTURWcUQc[SUR[cHSc^YcOU_WA". So, the input has each character xored with 0x3c and compared to this. To undo an xor, you simply xor again. Therefore, the flag is this string with each character xored with 0x3c. 

```python
>>> "".join(chr(ord(c)^0x3c) for c in "]_HZGUcHTURWcUQc[SUR[cHSc^YcOU_WA")
'actf{i_think_im_going_to_be_sick}'
```

## Flag

```
actf{i_think_im_going_to_be_sick}
```