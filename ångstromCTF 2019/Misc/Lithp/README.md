# Lithp
Misc (50 points, 636 solves)

## Challenge 

My friend gave me this [program](https://files.actf.co/b7bb1a50e52ba3f9ff93f4d08691a7eef81457410192f769b076a3052ff21b21/lithp.lisp) but I couldn't understand what he was saying - what was he trying to tell me?

Author: fireholder

## Solution

We are given a Lisp file called "lithp.lisp". Lisp (List Processor) is a language based on lists. I found this [LISP Tutorial](https://www.tutorialspoint.com/lisp/) to be very useful because I had not looked at LISP in quite some time. First, we can rewrite this in a language we are more familiar with. 

The code has some variables at the top, then some functions. A quick look at the code shows that each function calls the one below it. So, I started at the bottom and worked up. 

```lisp
(defun whats-this (x y)
    (cond
        ((equal y 0) 0)
        (t (+ (whats-this x (- y 1)) x))))
```
This is rather basic Lisp and translates to this Python:
```python
def whats_this(x, y):
   if y == 0:
      return 0
   return whats_this(x, y-1) + x
```

Some basic common sense and perhaps some testing tells us that this function is simply doing multiplication. 

```lisp
(defun owo (inpth)
    (setf out nil)
    (do ((redth *reorder* (cdr redth)))
        ((null redth) out)
        (setq out (append out (list (nth (car redth) inpth))))))
```
This one is a bit more complicated. An important part to understand is that `car` will take the first item in a list, and `cdr` will take the rest. The `do` construct performs iteration using the variable `redth` set to *reorder* and setting it to `cdr redth` (everything after the first item) after each iteration. This basically iterates through *reorder*. Once `redth` is null (there are no more items), `out` is returned.
```python
def owo(inpth):
   out = []
   for n in reorder:
      out.append(inpth[n])
   return out
```
This function reorders the items in inpth by setting each item `k` to `input[**reorder[k]]`.

```lisp
(defun multh (plain)
    (cond
        ((null plain) nil)
        (t (cons (whats-this (- 1 (car plain)) (car plain)) (multh (cdr plain))))))
```
This is also quite simple Lisp. Writing out the `car` and `cdr` operations might help. 
```python
def multh(plain):
   if plain == "":
      return []
   return [whats(plain[0]-1, plain[0])] + multh(plain[1:])
```
This function returns a list with `whats(plain-1, plain)` for each item in `plain`. We saw that `whats` is just multiplication, so this function is just calculates `n(n-1)` for each `n` in `plain`. 

```lisp
(defun enc (plain)
    (setf uwuth (multh plain))
    (setf uwuth (owo uwuth))
    (setf out nil)
    (dotimes (ind (length plain) out)
        (setq out (append out (list (/ (nth ind uwuth) -1))))))
```
This function puts all the above to use. I wasn't quite sure what the last two lines were supposed to do. They look like dividing each element by -1 but that wouldn't give the right answer since all of the flag is positive. I chose to just ignore it and it worked okay. 
```python
def enc(plain):
   uwuth = multh(plain)
   uwuth = owo(uwuth)
   return uwuth
```
Combining all of the code, we can see that `enc` first turns each element `n` into `n(n-1)`, then reorders them based on *reorder*. 

These operations are all reversible. `multh` can be reversed with the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula). `n(n-1)=k` simplifies to `n^2-n-k=0`, so `k=(sqrt(4n+1)-1)/2`. To undo the reorder, we can set each `out[reorder[k]]` to `input[k]`. 

With all this information, I wrote a [script](solve.py) to solve for the flag. 

## Flag

```
actf{help_me_I_have_a_lithp}
```