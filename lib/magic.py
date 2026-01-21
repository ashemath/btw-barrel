import socket
word = socket.gethostname()
key = ord(word[-1])

with open("/usr/local/lib/barrel/barrel.payload") as payload:
    lines = payload.readlines()
payload.close()

for line in lines:
    output = ""
    for ch in line:
        output += chr(ord(ch) - key)
    print(output)
