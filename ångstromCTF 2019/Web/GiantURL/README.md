# GiantURL
Web (190 points, 21 solves)

## Challenge 

Have you ever wished your URLs were longer? No? Well here's [a site](https://giant_url.2019.chall.actf.co/) that does it anyways ([source](https://files.actf.co/a87101449acbef8a7a655fa32a1d7203b674c1101389875b7ca240e768cbb262/gianturl.php)).

Note: the admin does visit the URL you have lengthened.

Author: kmh11

## Hint

With all these new browser features, you don't even need CSRF tokens anymore!

## Solution

Note: I did not solve this during the contest. 

The hint tells us that this is probably a CSRF attack. Taking a look at the source code, we see that we can make a request to `/admin/changepass` to change the password if the request is made from the admin's session. I initially created my own page that would POST to this endpoint, but this is blocked by CSP.

```
Content-Security-Policy: default-src 'self'; style-src 'unsafe-inline';
```

So, the request has to come from the site itself. But where can we make this request? We look for places we can put user input and we find that the redirect page just echoes the URL we enter into the `href` attribute without quotes. So, we can break out of the `href` with a single space and add whatever attributes we want. 

Apparently there is a `ping` [attribute](https://www.w3schools.com/tags/att_a_ping.asp) that does exactly what we want. When the link is clicked, it sends a POST request. It doesn't matter that no parameters are sent because the change password code only checks in `$_REQUEST` (both POST and GET). So, we can set the ping to send a POST request to `/admin/changepass/?password=PASSWORD`. The password we set it to has to be long enough to pass the "security checks". 

First, we lengthen a URL with the `ping` attribute.

```
https://xkcd.com ping=/admin/changepass?password=I%20like%20CTF%20but%20I%20am%20bad%20at%20CTF%20so%20I%20have%20upperclassmen%20carry%20me%20in%20CTF%20actually%20not%20really%20they%20are%20lazy%20and%20do%20not%20help%20me%20so%20I%20am%20just%20sad
```

Send the lengthened URL to the admin, which should change the password. Then, go to `/admin` and log in with your new password. 

## Flag

```
actf{p1ng_p0ng_9b05891fa9c3bed74d02a349877b1c60}
```
