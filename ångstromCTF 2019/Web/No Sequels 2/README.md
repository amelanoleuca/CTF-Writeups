# No Sequels 2
Web (80 points, 167 solves)

## Challenge 

This is the sequel to [No Sequels](https://nosequels.2019.chall.actf.co/). You'll see the challenge page once you solve the first one.

Author: Sirlan

## Solution

The challenge asks us to get the `admin` password. Now that we know we can inject JSON into our fields, we need to figure out what the value of the fields are. We know that `username` has to be `admin` from the challenge. But how can we figure out the password?

MongoDB also supports [regular expressions](https://docs.mongodb.com/manual/reference/operator/query/regex/). We can use this to our advantage because we can guess each character of the flag in sequence. 

```json
{
   "username": "admin",
   "password": {"$regex": "^a"}
}
```

The `^` means the beginning of the string. This regex looks for an `a` at the beginning of the string. We send this and get a "Wrong username or password". So, we change the `a` to `b` and try again. When that doesn't work, we try `c` and get a success message. This tells us that the first letter of the password is c. 

Now we just continue this pattern, by adding a letter to the end. Eventually, we try this payload:

```json
{
   "username": "admin",
   "password": {"$regex": "^co"}
}
```

This is successful. In this manner, we can keep trying letters until we get the entire string. With all this information, I wrote a [script](solve.py) to solve for the password. 

Submitting the password gives us our flag. 

## Flag

```
actf{still_no_sql_in_the_sequel}
```
