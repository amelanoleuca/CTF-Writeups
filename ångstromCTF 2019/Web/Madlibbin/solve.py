globals = "{'__name__': 'werkzeug.datastructures', '__doc__': '\n    werkzeug.datastructures\n    ~~~~~~~~~~~~~~~~~~~~~~~\n\n    This module provides mixins and classes with an immutable interface.\n\n    :copyright: 2007 Pallets\n    :license: BSD-3-Clause\n', '__package__': 'werkzeug', '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7ff11f9de9e8>, '__spec__': ModuleSpec(name='werkzeug.datastructures', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7ff11f9de9e8>, origin='/usr/local/lib/python3.7/site-packages/werkzeug/datastructures.py'), '__file__': '/usr/local/lib/python3.7/site-packages/werkzeug/datastructures.py', '__cached__': '/usr/local/lib/python3.7/site-packages/werkzeug/__pycache__/datastructures.cpython-37.pyc', '__builtins__': {'__name__': 'builtins', '__doc__': \"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.\", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>), '__build_class__': <built-in function __build_class__>, '__import__': <built-in function __import__>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'breakpoint': <built-in function breakpoint>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>, 'delattr': <built-in function delattr>, 'dir': <built-in function dir>, 'divmod': <built-in function divmod>, 'eval': <built-in function eval>, 'exec': <built-in function exec>, 'format': <built-in function format>, 'getattr': <built-in function getattr>, 'globals': <built-in function globals>, 'hasattr': <built-in function hasattr>, 'hash': <built-in function hash>, 'hex': <built-in function hex>, 'id': <built-in function id>, 'input': <built-in function input>, 'isinstance': <built-in function isinstance>, 'issubclass': <built-in function issubclass>, 'iter': <built-in function iter>, 'len': <built-in function len>, 'locals': <built-in function locals>, 'max': <built-in function max>, 'min': <built-in function min>, 'next': <built-in function next>, 'oct': <built-in function oct>, 'ord': <built-in function ord>, 'pow': <built-in function pow>, 'print': <built-in function print>, 'repr': <built-in function repr>, 'round': <built-in function round>, 'setattr': <built-in function setattr>, 'sorted': <built-in function sorted>, 'sum': <built-in function sum>, 'vars': <built-in function vars>, 'None': None, 'Ellipsis': Ellipsis, 'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': <class 'bool'>, 'memoryview': <class 'memoryview'>, 'bytearray': <class 'bytearray'>, 'bytes': <class 'bytes'>, 'classmethod': <class 'classmethod'>, 'complex': <class 'complex'>, 'dict': <class 'dict'>, 'enumerate': <class 'enumerate'>, 'filter': <class 'filter'>, 'float': <class 'float'>, 'frozenset': <class 'frozenset'>, 'property': <class 'property'>, 'int': <class 'int'>, 'list': <class 'list'>, 'map': <class 'map'>, 'object': <class 'object'>, 'range': <class 'range'>, 'reversed': <class 'reversed'>, 'set': <class 'set'>, 'slice': <class 'slice'>, 'staticmethod': <class 'staticmethod'>, 'str': <class 'str'>, 'super': <class 'super'>, 'tuple': <class 'tuple'>, 'type': <class 'type'>, 'zip': <class 'zip'>, '__debug__': True, 'BaseException': <class 'BaseException'>, 'Exception': <class 'Exception'>, 'TypeError': <class 'TypeError'>, 'StopAsyncIteration': <class 'StopAsyncIteration'>, 'StopIteration': <class 'StopIteration'>, 'GeneratorExit': <class 'GeneratorExit'>, 'SystemExit': <class 'SystemExit'>, 'KeyboardInterrupt': <class 'KeyboardInterrupt'>, 'ImportError': <class 'ImportError'>, 'ModuleNotFoundError': <class 'ModuleNotFoundError'>, 'OSError': <class 'OSError'>, 'EnvironmentError': <class 'OSError'>, 'IOError': <class 'OSError'>, 'EOFError': <class 'EOFError'>, 'RuntimeError': <class 'RuntimeError'>, 'RecursionError': <class 'RecursionError'>, 'NotImplementedError': <class 'NotImplementedError'>, 'NameError': <class 'NameError'>, 'UnboundLocalError': <class 'UnboundLocalError'>, 'AttributeError': <class 'AttributeError'>, 'SyntaxError': <class 'SyntaxError'>, 'IndentationError': <class 'IndentationError'>, 'TabError': <class 'TabError'>, 'LookupError': <class 'LookupError'>, 'IndexError': <class 'IndexError'>, 'KeyError': <class 'KeyError'>, 'ValueError': <class 'ValueError'>, 'UnicodeError': <class 'UnicodeError'>, 'UnicodeEncodeError': <class 'UnicodeEncodeError'>, 'UnicodeDecodeError': <class 'UnicodeDecodeError'>, 'UnicodeTranslateError': <class 'UnicodeTranslateError'>, 'AssertionError': <class 'AssertionError'>, 'ArithmeticError': <class 'ArithmeticError'>, 'FloatingPointError': <class 'FloatingPointError'>, 'OverflowError': <class 'OverflowError'>, 'ZeroDivisionError': <class 'ZeroDivisionError'>, 'SystemError': <class 'SystemError'>, 'ReferenceError': <class 'ReferenceError'>, 'MemoryError': <class 'MemoryError'>, 'BufferError': <class 'BufferError'>, 'Warning': <class 'Warning'>, 'UserWarning': <class 'UserWarning'>, 'DeprecationWarning': <class 'DeprecationWarning'>, 'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>, 'SyntaxWarning': <class 'SyntaxWarning'>, 'RuntimeWarning': <class 'RuntimeWarning'>, 'FutureWarning': <class 'FutureWarning'>, 'ImportWarning': <class 'ImportWarning'>, 'UnicodeWarning': <class 'UnicodeWarning'>, 'BytesWarning': <class 'BytesWarning'>, 'ResourceWarning': <class 'ResourceWarning'>, 'ConnectionError': <class 'ConnectionError'>, 'BlockingIOError': <class 'BlockingIOError'>, 'BrokenPipeError': <class 'BrokenPipeError'>, 'ChildProcessError': <class 'ChildProcessError'>, 'ConnectionAbortedError': <class 'ConnectionAbortedError'>, 'ConnectionRefusedError': <class 'ConnectionRefusedError'>, 'ConnectionResetError': <class 'ConnectionResetError'>, 'FileExistsError': <class 'FileExistsError'>, 'FileNotFoundError': <class 'FileNotFoundError'>, 'IsADirectoryError': <class 'IsADirectoryError'>, 'NotADirectoryError': <class 'NotADirectoryError'>, 'InterruptedError': <class 'InterruptedError'>, 'PermissionError': <class 'PermissionError'>, 'ProcessLookupError': <class 'ProcessLookupError'>, 'TimeoutError': <class 'TimeoutError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'copyright': Copyright (c) 2001-2019 Python Software Foundation.All Rights Reserved.Copyright (c) 2000 BeOpen.com.All Rights Reserved.Copyright (c) 1995-2001 Corporation for National Research Initiatives.All Rights Reserved.Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.All Rights Reserved., 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands    for supporting Python development.  See www.python.org for more information., 'license': Type license() to see the full license text, 'help': Type help() for interactive help, or help(object) for help about object.}, 'codecs': <module 'codecs' from '/usr/local/lib/python3.7/codecs.py'>, 'mimetypes': <module 'mimetypes' from '/usr/local/lib/python3.7/mimetypes.py'>, 're': <module 're' from '/usr/local/lib/python3.7/re.py'>, 'deepcopy': <function deepcopy at 0x7ff1209f2730>, 'repeat': <class 'itertools.repeat'>, 'BytesIO': <class '_io.BytesIO'>, 'collections_abc': <module 'collections.abc' from '/usr/local/lib/python3.7/collections/abc.py'>, 'integer_types': (<class 'int'>,), 'iteritems': <function <lambda> at 0x7ff11fe8e6a8>, 'iterkeys': <function <lambda> at 0x7ff11fe8e488>, 'iterlists': <function <lambda> at 0x7ff11fe8e730>, 'itervalues': <function <lambda> at 0x7ff11fe8e620>, 'make_literal_wrapper': <function make_literal_wrapper at 0x7ff11fe8e8c8>, 'PY2': False, 'string_types': (<class 'str'>,), 'text_type': <class 'str'>, 'to_native': <function to_native at 0x7ff11fe8eb70>, '_missing': no value, 'get_filesystem_encoding': <function get_filesystem_encoding at 0x7ff11f996b70>, '_locale_delim_re': re.compile('[_-]'), 'is_immutable': <function is_immutable at 0x7ff11f9e7a60>, 'iter_multi_items': <function iter_multi_items at 0x7ff11f996c80>, 'native_itermethods': <function native_itermethods at 0x7ff11f996d08>, 'ImmutableListMixin': <class 'werkzeug.datastructures.ImmutableListMixin'>, 'ImmutableList': <class 'werkzeug.datastructures.ImmutableList'>, 'ImmutableDictMixin': <class 'werkzeug.datastructures.ImmutableDictMixin'>, 'ImmutableMultiDictMixin': <class 'werkzeug.datastructures.ImmutableMultiDictMixin'>, 'UpdateDictMixin': <class 'werkzeug.datastructures.UpdateDictMixin'>, 'TypeConversionDict': <class 'werkzeug.datastructures.TypeConversionDict'>, 'ImmutableTypeConversionDict': <class 'werkzeug.datastructures.ImmutableTypeConversionDict'>, 'ViewItems': <class 'werkzeug.datastructures.ViewItems'>, 'MultiDict': <class 'werkzeug.datastructures.MultiDict'>, '_omd_bucket': <class 'werkzeug.datastructures._omd_bucket'>, 'OrderedMultiDict': <class 'werkzeug.datastructures.OrderedMultiDict'>, '_options_header_vkw': <function _options_header_vkw at 0x7ff11f996d90>, '_unicodify_header_value': <function _unicodify_header_value at 0x7ff11f9b7620>, 'Headers': <class 'werkzeug.datastructures.Headers'>, 'ImmutableHeadersMixin': <class 'werkzeug.datastructures.ImmutableHeadersMixin'>, 'EnvironHeaders': <class 'werkzeug.datastructures.EnvironHeaders'>, 'CombinedMultiDict': <class 'werkzeug.datastructures.CombinedMultiDict'>, 'FileMultiDict': <class 'werkzeug.datastructures.FileMultiDict'>, 'ImmutableDict': <class 'werkzeug.datastructures.ImmutableDict'>, 'ImmutableMultiDict': <class 'werkzeug.datastructures.ImmutableMultiDict'>, 'ImmutableOrderedMultiDict': <class 'werkzeug.datastructures.ImmutableOrderedMultiDict'>, 'Accept': <class 'werkzeug.datastructures.Accept'>, 'MIMEAccept': <class 'werkzeug.datastructures.MIMEAccept'>, 'LanguageAccept': <class 'werkzeug.datastructures.LanguageAccept'>, 'CharsetAccept': <class 'werkzeug.datastructures.CharsetAccept'>, 'cache_property': <function cache_property at 0x7ff11f9ba378>, '_CacheControl': <class 'werkzeug.datastructures._CacheControl'>, 'RequestCacheControl': <class 'werkzeug.datastructures.RequestCacheControl'>, 'ResponseCacheControl': <class 'werkzeug.datastructures.ResponseCacheControl'>, 'CallbackDict': <class 'werkzeug.datastructures.CallbackDict'>, 'HeaderSet': <class 'werkzeug.datastructures.HeaderSet'>, 'ETags': <class 'werkzeug.datastructures.ETags'>, 'IfRange': <class 'werkzeug.datastructures.IfRange'>, 'Range': <class 'werkzeug.datastructures.Range'>, 'ContentRange': <class 'werkzeug.datastructures.ContentRange'>, 'Authorization': <class 'werkzeug.datastructures.Authorization'>, 'WWWAuthenticate': <class 'werkzeug.datastructures.WWWAuthenticate'>, 'FileStorage': <class 'werkzeug.datastructures.FileStorage'>, 'exceptions': <module 'werkzeug.exceptions' from '/usr/local/lib/python3.7/site-packages/werkzeug/exceptions.py'>, 'dump_header': <function dump_header at 0x7ff11f8d7400>, 'dump_options_header': <function dump_options_header at 0x7ff11f8d7378>, 'generate_etag': <function generate_etag at 0x7ff11f8d7bf8>, 'http_date': <function http_date at 0x7ff11f8d7e18>, 'is_byte_range_valid': <function is_byte_range_valid at 0x7ff11f8d5400>, 'parse_options_header': <function parse_options_header at 0x7ff11f8d7598>, 'parse_set_header': <function parse_set_header at 0x7ff11f8d7730>, 'quote_etag': <function quote_etag at 0x7ff11f8d7a60>, 'quote_header_value': <function quote_header_value at 0x7ff11f8d7268>, 'unquote_etag': <function unquote_etag at 0x7ff11f8d7ae8>}"

hasos = """
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
"""

hasos = [l.split(":")[0] for l in hasos.split("\n")]

for module in hasos:
	if module in globals:
		print(module)