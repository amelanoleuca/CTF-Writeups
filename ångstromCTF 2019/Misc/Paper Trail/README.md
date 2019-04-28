# Paper Trail
Misc (50 points, 636 solves)

## Challenge 

Something is suspicious about defund's math papers. See if you can find anything in the [network packets](https://files.actf.co/8e1122c1c15f2373fb6e98c207c3218ecd322796a2e2275f4b99e7bb21b9e253/paper_trail.pcapng) we've intercepted from his computer.

Author: defund

## Solution

We are given a Wireshark capture called "paper_trail.pcapng". Opening the capture, we see that it appears to be several IRC messages. They are first sent and then echoed back by the servo. The messages are not encrypted or encoded, so we can just read them. 

```
defund :I have to confide in someone, even if it's myself
defund :my publications are all randomly generated :(
defund :a
defund :c
defund :t
defund :f
defund :{
defund :f
defund :a
defund :k
defund :e
defund :_
defund :m
defund :a
defund :t
defund :h
defund :_
defund :p
defund :a
defund :p
defund :e
defund :r
defund :s
defund :}

## Flag

```
actf{fake_math_papers}
```