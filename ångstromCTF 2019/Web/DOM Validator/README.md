# DOM Validator
Web (130 points, 76 solves)

## Challenge 

Always remember to [validate your DOMs](https://files.actf.co/a5a40782725efedbdcc7d67ccae74f2ea82cec820d611c1fa5bd9423cc85f724/index.js) before you [render them](https://dom.2019.chall.actf.co/).

Author: kmh11

## Solution

Note: I did not solve this during the contest. 

Looking at the source code, it looks like it writes our input to a static HTML file (so no SSTI). But, there doesn't seem to be any validation on the post body so we can just use a `<script>` and use XSS right?

Posting `<script>alert()</script>` doesn't give an error and it shows up in the source code, but nothing shows up. Why is that?

```html
<!DOCTYPE html SYSTEM "3b16c602b53a3e4fc22f0d25cddb0fc4d1478e0233c83172c36d0a6cf46c171ed5811fbffc3cb9c3705b7258179ef11362760d105fb483937607dd46a6abcffc">
<html>
	<head>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css">
		<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/sha512.js"></script>
		<script src="../scripts/DOMValidator.js"></script>
	</head>
	<body>
		<h1>random name</h1>
		<p><script>alert()</script></p>
	</body>
</html>
```

Most of the content looks pretty standard, except for the `DOMValidator.js` script. Opening it up, we see what it does. 

```js
function checksum (element) {
	var string = ''
	string += (element.attributes ? element.attributes.length : 0) + '|'
	for (var i = 0; i < (element.attributes ? element.attributes.length : 0); i++) {
		string += element.attributes[i].name + ':' + element.attributes[i].value + '|'
	}
	string += (element.childNodes ? element.childNodes.length : 0) + '|'
	for (var i = 0; i < (element.childNodes ? element.childNodes.length : 0); i++) {
		string += checksum(element.childNodes[i]) + '|'
	}
	return CryptoJS.SHA512(string).toString(CryptoJS.enc.Hex)
}
var request = new XMLHttpRequest()
request.open('GET', location.href, false)
request.send(null)
if (checksum((new DOMParser()).parseFromString(request.responseText, 'text/html')) !== document.doctype.systemId) {
	document.documentElement.remove()
}
```

This script is in the `<head>`, so it will run before the body loads. It will use a `DOMParser` to parse the structure of the page first, then feed it into the `checksum` function. If it doesn't match the hash hard-coded into the page, then it will delete the body and nothing will render. This makes our XSS useless. 

So, I looked into many different ways of injecting code without using HTML tags, none of which worked. 

The intended solution was to add a slash to the URL, something like this:

```
https://dom.2019.chall.actf.co/posts//random%20name.html
```

Express will interpret that double slash as one and still display the page, but the relative URL for `DOMValidator.js` is now broken. Opening this link, we can see our empty `alert()`. 

We know that the flag is in a cookie when we report a page to the admin, so we can just use XSS to send `document.cookie` somewhere. If you don't have the time or resources to write your own logger, [Weastie Hack Tools](https://www.weastie.com/hack_tools) has a good [HTTP Request Listener](https://www.weastie.com/hack_tools/listener), or you can use [XSS Hunter](https://xsshunter.com/). Simply put the payload into the body of the post, then report it to the admin with an extra slash like above. 

## Flag

```
actf{its_all_relative}
```
