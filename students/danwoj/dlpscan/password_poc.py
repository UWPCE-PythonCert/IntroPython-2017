>>> import nacl.pwhash
>>> password = b'my password'
>>> for i in range(4):
...     print(nacl.pwhash.str(password))
...
b'$argon2id$v=19$m=65536,t=2,p=1$...'
b'$argon2id$v=19$m=65536,t=2,p=1$...'
b'$argon2id$v=19$m=65536,t=2,p=1$...'
b'$argon2id$v=19$m=65536,t=2,p=1$...'
>>>
>>> # if needed, each hasher is exposed
... # in just the same way:
... for i in range(4):
...     print(nacl.pwhash.scrypt.str(password))
...
b'$7$C6..../...'
b'$7$C6..../...'
b'$7$C6..../...'
b'$7$C6..../...'
>>>
>>> for i in range(4):
...     print(nacl.pwhash.argon2i.str(password))
...
b'$argon2i$v=19$m=32768,t=4,p=1$...'
b'$argon2i$v=19$m=32768,t=4,p=1$...'
b'$argon2i$v=19$m=32768,t=4,p=1$...'
b'$argon2i$v=19$m=32768,t=4,p=1$...'
>>>
>>> # and
...
>>> for i in range(4):
...     print(nacl.pwhash.argon2id.str(password))