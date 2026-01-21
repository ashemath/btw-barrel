# btw-barrel

Lock down access to a single website. No web browser
needs to be installed. The "browser" exists as a consequence
of a couple Python packages and an obfuscted script.

If a user wants to figure out how to reverse the obfuscation
instead of what they're supposed to be doing, we'll
leave that as an exercise for the reader.

browser.py launches a little browser-like program that "pins"
the user to a single URL. Downloading files works, but
it's nothing like a regular web-browser. If a user tries to load
a page anywhere that is not "allowed," it goes, but proceeds to go immediately
"back".

But Bill, the user can just copy the script and edit it!
No, it's not that easy.

The install script copies the deobfuscation script and the obfuscated
code to a readable directory.

A user could figured out how to run the deobfuscating script, but this
would be hard to do without leaving a trail or being observed.

Just trying to make deobfusction trickier for someone in a restricted-net-
access type situation work harder.

`browser.py`: this is our simple "browser" application. To be lazily encrypted!
`magic.py`: how we reverse the encryption.
`barrel.py`: now you see it?
`run_browser.sh`: now you don't!

`run_browser.sh` 
