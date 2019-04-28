# TI-1337
Misc (250 points, 12 solves)

## Challenge 

I've gotten ahold of a prototype of TI's latest calculator: the [TI-1337](https://files.actf.co/9612c7eb4e10ca428e0bcb50444f1ce491942a8bba13a2455e2a38c7a1aa5027/ti1337.zip). It only seems to work on integers though...

Connect with `nc 54.159.113.26 19304`.

Author: kmh11

## Solution

Note: I did not solve this during the contest. 

A quick look at the source code shows us that the service is just a very restricted Python shell. We can set variables and use mathematical operations, and then the calculator will evaluate it all and output the variables. 

In `wrapper.py`, we are told that we can not use any of these characters:

```
()[]{}_.#\"\'\\ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

So what can we use? I immediately thought of `:`, which lets use create [lambda functions](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/). But, I could not think of anything that this could be used with. Lambda functions alone are not enough to get the flag.

After the contest ended, I learned about [class decorators](https://krzysztofzuraw.com/blog/2016/python-class-decorators.html). To use class decorators, you need the `@` symbol, which is not restricted! We can use decorators to execute single-paramter functions, which is all we need. 

Our target is to get the Python shell to print `open("flag.txt").read()`. In order to get a string without using quotes, we can give it a list of numbers instead and use `bytes`. It would be great to just `eval` this directly, but we can't pass arguments to the decorators directly. We can use a lambda function to ignore the input and return the numbers, then feed that into `bytes` and then `eval`. 

```python
x = 111, 112, 101, 110, 40, 34, 102, 108, 97, 103, 46, 116, 120, 116, 34, 41, 46, 114, 101, 97, 100, 40, 41
y = lambda z: x
@print
@eval
@bytes
@y
class asdf: pass
```

This is the same as this:

```python
print(eval(bytes(y(asdf))))
```

## Flag

```
actf{some_wonderful_decorations}
```