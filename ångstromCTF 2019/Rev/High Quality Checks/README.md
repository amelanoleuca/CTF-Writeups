# High Quality Checks
Rev (110 points, 269 solves)

## Challenge 

After two break-ins to his shell server, kmh got super paranoid about a third! He's so paranoid that he abandoned the traditional password storage method and came up with [this](https://files.actf.co/6f9ff36334b1c8be130f5fd13d6d77c1de6f546512d1421370fc874948d6e37c/high_quality_checks) monstrosity! I reckon he used the flag as the password, can you find it?

Author: Aplet123

## Solution

We are given an executable file. Using `file`, we find that it is an unstripped 64-bit Linux ELF. 

```
$ file high_quality_checks
high_quality_checks: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=e7556b55e0c73b4de8b3f387571dd59c3535a0ee, not stripped
```

When we run the program, it asks us for a string. Entering in some random text outputs "Flag is too short". After giving it a longer flag, it outputs "That's not the flag."

Opening it up in peda, we see some functions called b, d, e, k, n, o, s, u, v, w, and z.

Yikes.

![One-letter identifiers have their place!](https://pics.me.me/descriptive-names-cryptic-names-alljust-oneletter-onevariable-imgiip-com-variable-names-32484923.png)

We can start at `main` again. It looks relatively simple.

```
gdb-peda$ disas main
Dump of assembler code for function main:
   0x0000000000400a5b <+0>:	push   rbp
   0x0000000000400a5c <+1>:	mov    rbp,rsp
   0x0000000000400a5f <+4>:	sub    rsp,0x20
   0x0000000000400a63 <+8>:	mov    rax,QWORD PTR fs:0x28
   0x0000000000400a6c <+17>:	mov    QWORD PTR [rbp-0x8],rax
   0x0000000000400a70 <+21>:	xor    eax,eax
   0x0000000000400a72 <+23>:	lea    rdi,[rip+0x10b]        # 0x400b84
   0x0000000000400a79 <+30>:	call   0x4004e0 <puts@plt>
   0x0000000000400a7e <+35>:	lea    rax,[rbp-0x20]
   0x0000000000400a82 <+39>:	mov    rsi,rax
   0x0000000000400a85 <+42>:	lea    rdi,[rip+0x10a]        # 0x400b96
   0x0000000000400a8c <+49>:	mov    eax,0x0
   0x0000000000400a91 <+54>:	call   0x400510 <__isoc99_scanf@plt>
   0x0000000000400a96 <+59>:	lea    rax,[rbp-0x20]
   0x0000000000400a9a <+63>:	mov    rdi,rax
   0x0000000000400a9d <+66>:	call   0x4004f0 <strlen@plt>
   0x0000000000400aa2 <+71>:	cmp    rax,0x12
   0x0000000000400aa6 <+75>:	ja     0x400abb <main+96>
   0x0000000000400aa8 <+77>:	lea    rdi,[rip+0xec]        # 0x400b9b
   0x0000000000400aaf <+84>:	call   0x4004e0 <puts@plt>
   0x0000000000400ab4 <+89>:	mov    eax,0x0
   0x0000000000400ab9 <+94>:	jmp    0x400aea <main+143>
   0x0000000000400abb <+96>:	lea    rax,[rbp-0x20]
   0x0000000000400abf <+100>:	mov    rdi,rax
   0x0000000000400ac2 <+103>:	call   0x40094a <check>
   0x0000000000400ac7 <+108>:	test   eax,eax
   0x0000000000400ac9 <+110>:	je     0x400ad9 <main+126>
   0x0000000000400acb <+112>:	lea    rdi,[rip+0xdc]        # 0x400bae
   0x0000000000400ad2 <+119>:	call   0x4004e0 <puts@plt>
   0x0000000000400ad7 <+124>:	jmp    0x400ae5 <main+138>
   0x0000000000400ad9 <+126>:	lea    rdi,[rip+0xe2]        # 0x400bc2
   0x0000000000400ae0 <+133>:	call   0x4004e0 <puts@plt>
   0x0000000000400ae5 <+138>:	mov    eax,0x0
   0x0000000000400aea <+143>:	mov    rdx,QWORD PTR [rbp-0x8]
   0x0000000000400aee <+147>:	xor    rdx,QWORD PTR fs:0x28
   0x0000000000400af7 <+156>:	je     0x400afe <main+163>
   0x0000000000400af9 <+158>:	call   0x400500 <__stack_chk_fail@plt>
   0x0000000000400afe <+163>:	leave  
   0x0000000000400aff <+164>:	ret    
End of assembler dump.
```

It appears to compare the length of the string to 0x12 (18). The flag must be longer than this. Next, it calls `check` and returns. Lets take a look at `check`.

```
gdb-peda$ disas check
Dump of assembler code for function check:
   0x000000000040094a <+0>:	push   rbp
   0x000000000040094b <+1>:	mov    rbp,rsp
   0x000000000040094e <+4>:	sub    rsp,0x8
   0x0000000000400952 <+8>:	mov    QWORD PTR [rbp-0x8],rdi
   0x0000000000400956 <+12>:	mov    rax,QWORD PTR [rbp-0x8]
   0x000000000040095a <+16>:	add    rax,0xc
   0x000000000040095e <+20>:	mov    rdi,rax
   0x0000000000400961 <+23>:	call   0x4008e5 <d>
   0x0000000000400966 <+28>:	test   eax,eax
   0x0000000000400968 <+30>:	je     0x400a54 <check+266>
   0x000000000040096e <+36>:	mov    rax,QWORD PTR [rbp-0x8]
   0x0000000000400972 <+40>:	movzx  eax,BYTE PTR [rax]
   0x0000000000400975 <+43>:	movsx  eax,al
   0x0000000000400978 <+46>:	mov    edi,eax
   0x000000000040097a <+48>:	call   0x400653 <v>
   0x000000000040097f <+53>:	test   eax,eax
   0x0000000000400981 <+55>:	je     0x400a54 <check+266>
   0x0000000000400987 <+61>:	mov    rax,QWORD PTR [rbp-0x8]
   0x000000000040098b <+65>:	add    rax,0x11
   0x000000000040098f <+69>:	movzx  eax,BYTE PTR [rax]
   0x0000000000400992 <+72>:	movsx  edx,al
   0x0000000000400995 <+75>:	mov    rax,QWORD PTR [rbp-0x8]
   0x0000000000400999 <+79>:	add    rax,0x10
   0x000000000040099d <+83>:	movzx  eax,BYTE PTR [rax]
   0x00000000004009a0 <+86>:	movsx  eax,al
   0x00000000004009a3 <+89>:	mov    esi,edx
   0x00000000004009a5 <+91>:	mov    edi,eax
   0x00000000004009a7 <+93>:	call   0x400900 <u>
   0x00000000004009ac <+98>:	test   eax,eax
   0x00000000004009ae <+100>:	je     0x400a54 <check+266>
   0x00000000004009b4 <+106>:	mov    rax,QWORD PTR [rbp-0x8]
   0x00000000004009b8 <+110>:	add    rax,0x5
   0x00000000004009bc <+114>:	movzx  eax,BYTE PTR [rax]
   0x00000000004009bf <+117>:	movsx  eax,al
   0x00000000004009c2 <+120>:	mov    edi,eax
   0x00000000004009c4 <+122>:	call   0x400748 <k>
   0x00000000004009c9 <+127>:	test   eax,eax
   0x00000000004009cb <+129>:	jne    0x400a54 <check+266>
   0x00000000004009d1 <+135>:	mov    rax,QWORD PTR [rbp-0x8]
   0x00000000004009d5 <+139>:	add    rax,0x9
   0x00000000004009d9 <+143>:	movzx  eax,BYTE PTR [rax]
   0x00000000004009dc <+146>:	movsx  eax,al
   0x00000000004009df <+149>:	mov    edi,eax
   0x00000000004009e1 <+151>:	call   0x400748 <k>
   0x00000000004009e6 <+156>:	test   eax,eax
   0x00000000004009e8 <+158>:	jne    0x400a54 <check+266>
   0x00000000004009ea <+160>:	mov    rax,QWORD PTR [rbp-0x8]
   0x00000000004009ee <+164>:	add    rax,0x1
   0x00000000004009f2 <+168>:	mov    rdi,rax
   0x00000000004009f5 <+171>:	call   0x400684 <w>
   0x00000000004009fa <+176>:	test   eax,eax
   0x00000000004009fc <+178>:	je     0x400a54 <check+266>
   0x00000000004009fe <+180>:	mov    rax,QWORD PTR [rbp-0x8]
   0x0000000000400a02 <+184>:	mov    esi,0x12
   0x0000000000400a07 <+189>:	mov    rdi,rax
   0x0000000000400a0a <+192>:	call   0x4006f6 <b>
   0x0000000000400a0f <+197>:	test   eax,eax
   0x0000000000400a11 <+199>:	je     0x400a54 <check+266>
   0x0000000000400a13 <+201>:	mov    rax,QWORD PTR [rbp-0x8]
   0x0000000000400a17 <+205>:	mov    esi,0x4
   0x0000000000400a1c <+210>:	mov    rdi,rax
   0x0000000000400a1f <+213>:	call   0x4006f6 <b>
   0x0000000000400a24 <+218>:	test   eax,eax
   0x0000000000400a26 <+220>:	je     0x400a54 <check+266>
   0x0000000000400a28 <+222>:	mov    rax,QWORD PTR [rbp-0x8]
   0x0000000000400a2c <+226>:	mov    esi,0x6c
   0x0000000000400a31 <+231>:	mov    rdi,rax
   0x0000000000400a34 <+234>:	call   0x40076d <z>
   0x0000000000400a39 <+239>:	test   eax,eax
   0x0000000000400a3b <+241>:	je     0x400a54 <check+266>
   0x0000000000400a3d <+243>:	mov    rax,QWORD PTR [rbp-0x8]
   0x0000000000400a41 <+247>:	mov    rdi,rax
   0x0000000000400a44 <+250>:	call   0x400889 <s>
   0x0000000000400a49 <+255>:	test   eax,eax
   0x0000000000400a4b <+257>:	je     0x400a54 <check+266>
   0x0000000000400a4d <+259>:	mov    eax,0x1
   0x0000000000400a52 <+264>:	jmp    0x400a59 <check+271>
   0x0000000000400a54 <+266>:	mov    eax,0x0
   0x0000000000400a59 <+271>:	leave  
   0x0000000000400a5a <+272>:	ret    
End of assembler dump.
```

Oh no. 

I originally did this problem with only peda, just like the other problems in this category. That is definitely possible, by `disas`ing all the functions and figuring out what they do. However, I have recently started using [ghidra](https://ghidra-sre.org/) and I think it makes this problem a whole lot easier. 

```c
undefined8 check(char *pcParm1)

{
  int iVar1;
  
  iVar1 = d(pcParm1 + 0xc);
  if ((((((iVar1 != 0) && (iVar1 = v((ulong)(uint)(int)*pcParm1), iVar1 != 0)) &&
        (iVar1 = u((ulong)(uint)(int)pcParm1[0x10],(ulong)(uint)(int)pcParm1[0x11],
                   (ulong)(uint)(int)pcParm1[0x11]), iVar1 != 0)) &&
       ((iVar1 = k((ulong)(uint)(int)pcParm1[5]), iVar1 == 0 &&
        (iVar1 = k((ulong)(uint)(int)pcParm1[9]), iVar1 == 0)))) &&
      ((iVar1 = w(pcParm1 + 1), iVar1 != 0 &&
       ((iVar1 = b(pcParm1,0x12), iVar1 != 0 && (iVar1 = b(pcParm1,4), iVar1 != 0)))))) &&
     ((iVar1 = z(pcParm1,0x6c), iVar1 != 0 && (iVar1 = s(pcParm1), iVar1 != 0)))) {
    return 1;
  }
  return 0;
}
```

Not a ton easier I guess. 

We can take this in parts. After a brief inspection, we can tell that everything in the `if` needs to be true to `return 1`.

For the rest of this writeup the nth character is 0-indexed unless otherwise stated. So the "first character" is really the second. 

`iVar1 != 0` is true if `d(*flag + 0xc)` is true. Lets take a look at `d`. 

```c
ulong d(int *piParm1)

{
  return (ulong)(*piParm1 == 0x30313763);
}
```

Easy! `d` simply returns if the parameter is equal to `0x30313763`. Therefore, the four characters of the flag starting at `0xc` must be "c710". 

Our flag is now ????????????c710???????????-->

`iVar1 = v((ulong)(uint)(int)*pcParm1), iVar1 != 0` is true if `v(*flag)` is true. Lets take a look at `v`. 

```c
ulong v(byte bParm1)

{
  int iVar1;
  
  iVar1 = n(0xac);
  return (ulong)((int)(char)(bParm1 ^ 0x37) == iVar1);
}
```

`v` returns if the first character xor 0x37 is equal to `n(0xac)`. So what does `n` do?

```c
ulong n(int iParm1)

{
  return (ulong)(uint)(iParm1 >> 1);
}
```

This is easy too! `n` just returns the parameter right shifted 1. Therefore, `v` returns if the first character xor 0x37 is equal to 0x56. With some simple math, we can find the first character to be "a".

Our flag is now a???????????c710???????????-->

`iVar1 = u((ulong)(uint)(int)pcParm1[0x10],(ulong)(uint)(int)pcParm1[0x11], (ulong)(uint)(int)pcParm1[0x11]), iVar1 != 0` is true if `u(flag[0x10], flag[0x11])` is true. Lets take a look at `u`. 

```c
undefined8 u(char cParm1,char cParm2)

{
  int iVar1;
  
  iVar1 = n(0xdc);
  if (((int)cParm1 == iVar1) && (iVar1 = o((ulong)(uint)(int)cParm2), iVar1 == 0x35053505)) {
    return 1;
  }
  return 0;
}
```

We remember that `n` just right shifts by 1. So, `u` tests if the first character is equal to n (0x6e, 0xdc>>1) and if o(second character) is equal to 0x35053505. What does `o` do?

```c
ulong o(char cParm1)

{
  int local_c;
  
  if (cParm1 < 'a') {
    local_c = (int)cParm1 + -0x30;
  }
  else {
    local_c = (int)cParm1 + -0x57;
  }
  local_c = (int)cParm1 * 0x100 + local_c;
  return (ulong)(uint)(local_c * 0x10001);
}
```

This is a little more interesting. If the character is less than a, it will subtract 0x30, otherwise it will subtract 0x57. Then, it will multiply the original character by 0x100 and add the subtracted value to itself. So, 0xab would become 0xab54. Then it will return this value multiplied by 0x10001, which does something similar. 0xabcd would become 0xabcdabcd. If the value we want at the end is 0x35053505, then it is easy to see that the value before returning is 0x3505 and the original character is 5 (0x35). 

Going back to `u(flag[0x10], flag[0x11])`, this tells us that the 16th character needs to be n and the 17th character needs to be 5. 

Our flag is now a???????????c710n5?????????-->

`iVar1 = k((ulong)(uint)(int)pcParm1[5]), iVar1 == 0` is true if `k(flag[5])` is false. Lets look at `k`. 

```c
ulong k(char cParm1)

{
  int iVar1;
  
  iVar1 = o((ulong)(uint)(int)cParm1);
  return (ulong)(iVar1 != 0x660f660f);
}
```

This checks if the `o(char)` is not 0x660f660f. Since we want this to be false, we want `o(char)` to be 0x660f660f. We looked at `o` already, so we know this character has to be "f" (0x66). 

Our flag is now a????f??????c710n5?????????-->

`iVar1 = k((ulong)(uint)(int)pcParm1[9]), iVar1 == 0` is true if `k(flag[9])` is false. But wait, we already did this!

Our flag is now a????f???f??c710n5?????????-->

`iVar1 = w(pcParm1 + 1), iVar1 != 0` is true if `w(flag+1)` is true. Lets look at `w`. 

```c
ulong w(char *pcParm1)

{
  return (ulong)((int)*pcParm1 + (int)pcParm1[2] * 0x10000 + (int)pcParm1[1] * 0x100 == 0x667463);
}
```

This takes the first characters, adds it to the second character * 0x100, then adds it to the third character * 0x10000. Basically, it is shifting the second character by two and the third character by four. This means the first character is "c" (0x63), the second character is "t" (0x74), and the third character is "f" (0x66). But, we started at the second character from the call to `w`.

Our flag is now actf?f???f??c710n5?????????-->

`iVar1 = b(pcParm1,0x12), iVar1 != 0` is true if `b(flag, 0x12)` is true. Lets look at `b`. 

```c
ulong b(long lParm1,uint uParm2)

{
  char cVar1;
  int iVar2;
  int iVar3;
  
  cVar1 = *(char *)(lParm1 + (long)(int)uParm2);
  iVar2 = n(0xf6);
  iVar3 = e((ulong)uParm2);
  return (ulong)((int)cVar1 == iVar3 * 2 + iVar2);
}
```

This checks if the 18th (0x12) character is equal to `e(0x12) * 2 + n(0xf6)`. We know that `n` just right shifts by 1, so that part is 0x7b. What does `e` do?

```c
ulong e(int iParm1)

{
  uint uVar1;
  
  uVar1 = (uint)(iParm1 >> 0x1f) >> 0x1e;
  uVar1 = (iParm1 + uVar1 & 3) - uVar1;
  return (ulong)(uint)((int)(uVar1 + (uVar1 >> 0x1f)) >> 1);
}
```

A `uint >> 0x1f >> 0x1e` is 0. 0x12 + 0 is 0x12, and 0x12 & 3 is 2. Then we return 2 >> 1, which is 1. 

Going back to `b`, we need the character to equal `e(0x12) * 2 + 0x7b`. Knowing the value of `e(0x12)`, we find that the character needs to be "}" (0x7d). 

Our flag is now actf?f???f??c710n5}

`iVar1 = b(pcParm1,4), iVar1 != 0` is true if `b(flag, 4)` is true. We looked at `b` already, so we know that it will check if the 4th character is `e(4)*2 + 0x7b`. We also looked at `e` already, so we know that this character must be "{" (0 + 0x7b). 

Our flag is now actf{f???f??c710n5}

`iVar1 = z(pcParm1,0x6c), iVar1 != 0` is true if `z(flag, 0x6c)` is true. Lets look at `z`. 

```c
undefined8 z(long lParm1,char cParm2)

{
  char cVar1;
  int iVar2;
  char local_17;
  char local_16;
  uint local_14;
  
  local_17 = 0;
  local_16 = 0;
  local_14 = 0;
  while ((int)local_14 < 8) {
    cVar1 = (char)(((int)cParm2 & 1 << ((byte)local_14 & 0x1f)) >> ((byte)local_14 & 0x1f));
    if ((local_14 & 1) == 0) {
      local_16 = local_16 +
                 (char)((int)cVar1 << ((byte)((int)(local_14 + (local_14 >> 0x1f)) >> 1) & 0x1f));
    }
    else {
      local_17 = local_17 +
                 (char)((int)cVar1 << ((byte)((int)(local_14 + (local_14 >> 0x1f)) >> 1) & 0x1f));
    }
    local_14 = local_14 + 1;
  }
  if ((((*(char *)(lParm1 + (long)local_17) == 'u') &&
       (cVar1 = *(char *)(lParm1 + (long)local_17 + 1), iVar2 = n(0xdc), (int)cVar1 == iVar2)) &&
      (cVar1 = *(char *)(lParm1 + (long)local_16), iVar2 = n(0xea), (int)cVar1 == iVar2)) &&
     (*(char *)(lParm1 + (long)local_16 + 1) == 'n')) {
    return 1;
  }
  return 0;
}
```

This is quite a bit larger than the last few functions. First it will loop through a counter from 0-7, calculating `cVar1` to be `(0x6c & (1 << counter)) >> counter`. Basically it will loop through the bits of 0x6c by anding it with a 1 shifted over some number of bits, then shifting it back down. If the counter is even, add the bit, shifted left counter/2 times to `local_16`, otherwise, add the bit, shifted left counter/2 times to `local_17`. After this, `local_16` contains the even bits of 0x6c (1010) and `local_17` contains the odd ones (0110). 

Lastly, it will check if the sixth (0110) character is "u", the seventh character that is "n" (`n(0xdc)` or 0x6e), the tenth (1010) character is "u" (`n(0xea)` or 0x75), and the eleventh character is "n". 

Our flag is now actf{fun?func710n5}

We could probably guess the flag at this point, but lets figure out our last check. 

`iVar1 = s(pcParm1), iVar1 != 0` is true if `s(flag)` is true. Lets look at `s`. 

```c
ulong s(long lParm1)

{
  int iVar1;
  int local_10;
  int local_c;
  
  local_10 = 0;
  local_c = 0;
  while (local_c < 0x13) {
    iVar1 = o((ulong)(uint)(int)*(char *)(lParm1 + (long)local_c));
    if (iVar1 == 0x5f2f5f2f) {
      local_10 = local_10 + local_c + 1;
    }
    local_c = local_c + 1;
  }
  return (ulong)(local_10 == 9);
}
```

This loops through a counter from 0-19 (0x13). It takes the character of the flag at the counter and calls `o` with that. It will check that against 0x5f2f5f2f. We looked at `o` already, so we know that this will be true if the character is "\_" (0x5f). If this is true, we add counter+1 to `local_10`. At the end, `local_10` needs to be 9. This tells us that the 9th character (this 9 is 1-indexed because we added counter+1 rather than counter) needs to be "\_". 

Our flag is now actf{fun_func710n5}

## Flag

```
actf{fun_func710n5}
```
