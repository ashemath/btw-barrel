# btw-barrel
PoC restricted web "browser" built with PyQt5.
Could've done it in PyQt6, but I plan to use it with obscure desktop
managers, so going with the older codebase.

git clone and run `sudo ./install.sh`. The browser is owned by
a `browser` user and has set guid enabled, so all users can launch the window with
`launch_browser.sh`.

A user without `sudo` will not be able to edit the script and adjust the `allow` list.
Instead of installing a real web browser, install btw-barrel's `launch_browser.sh` and
restrict access to exactly your target domains.

Designed as a reaction to the frustrating experience of trying to setup IP filtering to
restrict browsers to a certain enterprise LMS wed application.

Trying to account for every domain was challenging, and there is not guarantee that the list
will update fast enough. With this project, we monitor the page's URL instead of blocking
packets on the IP layer.

The browser gets to grab files from all over the world, yet the user stays navigating on my
allowed pages. The example is setup to force a user to browse wikipedia.org

## Permissions wackiness
I set a bunch of permissions on the browser script and a directory that holds the python and venv.
The purpose behind this is to make it a little bit harder to defeat the system.

I understand this is not a fool-proof system, but the idea is that I would deploy it in a monitored
context, one where command history is going to be recorded. Fits some uses for me, but you'll
want to look over this work and adapt it to your needs.
