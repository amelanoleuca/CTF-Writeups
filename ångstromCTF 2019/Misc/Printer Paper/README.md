# Printer Paper
Misc (150 points, 60 solves)

## Challenge 

We need to collect more of defund's math papers to gather evidence against him. See if you can find anything in the [data packets](https://files.actf.co/1c24f3f479ccb20bb2c0169497a7e59e6e9962b03aa5e25ca4a054cd1f4e114b/printer_paper.pcapng) we've intercepted from his printer.

Author: defund

## Hint

https://github.com/koenkooi/foo2zjs

## Solution

Note: I did not solve this during the contest. 

We are given a Wireshark capture with many USB packets. We are interested in the `URB_BULK out (completed)` packets. Looking through the first few ones, we can see some [PJL](https://en.wikipedia.org/wiki/Printer_Job_Language) packets (5, 7, 9).

```
%-12345X@PJL
@PJL JOB NAME = "paper.pdf" DISPLAY = "15 wiwang paper.pdf"
@PJL SET USERNAME = "wiwang"
@PJL SET DENSITY=3 
@PJL SET JAMRECOVERY=OFF 
@PJL SET ECONOMODE=OFF 
@PJL SET RET=MEDIUM 
%-12345X
```

After these packets, there is are several big 8224-length packets followed by a 3206-length packet, probably the remainder of the data after the first few chunks (15, 17, 19, 21, 23, 25, 27). Looking at these packets, there appear to be many `,XQX` headers. With the hint, we find that these are probably XQX packets. We export these to `paper.hex` and use `xxd` to turn them into binary files.

```
$ xxd -r -p paper.hex > paper.xqx
```

Next we decode this with `xqxdecode` like the hint suggests.

```
$ xqxdecode -d paper < paper.xqx
$ ls
paper-01-4.pbm  paper.hex  paper.xqx
```

We get a `paper-01-4.pbm` file. Using eog, we get the flag

```
$ eog paper-01-4.pbm
```

## Flag

```
actf{daniel_zhu_approves}
```