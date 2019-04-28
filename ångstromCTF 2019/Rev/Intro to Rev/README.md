# Intro to Rev
Rev (10 points, 963 solves)

## Challenge 

Many of our problems will require you to run Linux executable files (ELFs). This problem will help you figure out how to do it on our [shell server](https://2019.angstromctf.com/shell). Use your credentials to log in, then navigate to `/problems/2019/intro_to_rev`. Run the [executable](https://files.actf.co/755a950285e73554638600f46c485b2e90790d8c2f0642eb67c4716985ef9aa6/intro_to_rev) and follow its instructions to get a flag!

Author: Sirlan

## Hint

ELF files are run using `./filename`. You might also want to look into the `cd` and `ls` commands if you aren't familiar with Linux.

## Solution

Open the shell server, use `cd` to navigate to the directory in the problem, then run the program with `./intro_to_rev`. 

```
$ ./intro_to_rev
Welcome to your first reversing challenge!

If you are seeing this, then you already ran the file! Let's try some input next.
Enter the word 'angstrom' to continue:
angstrom
Good job! Some programs might also want you to enter information with a command line argument.

When you run a file, command line arguments are given by running './introToRev argument1 argument2' where you replace each argument with a desired string.

To get the flag for this problem, run this file again with the arguments 'binary' and 'reversing' (don't put the quotes).

$ ./intro_to_rev binary reversing
Welcome to your first reversing challenge!

If you are seeing this, then you already ran the file! Let's try some input next.
Enter the word 'angstrom' to continue:
angstrom
Good job! Some programs might also want you to enter information with a command line argument.

When you run a file, command line arguments are given by running './introToRev argument1 argument2' where you replace each argument with a desired string.

Good job, now go solve some real problems!
actf{this_is_only_the_beginning}
```

## Flag

```
actf{this_is_only_the_beginning}
```