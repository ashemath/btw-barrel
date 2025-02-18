#!/bin/sh

useradd browser
apt install -y qt5dxcb-plugin

if [ -d ./venv ]; then
    echo "venv exists!"
else
    echo "making venv now!";
    python3 -m venv venv
fi

chown -R browser:browser venv/

if [ -e ./venv/bin/activate ]; then
    echo "Activating!"
    . venv/bin/activate
else
    echo "Cannot activate!"
fi

if [ -e venv/lib/python3.11/site-packages/PyQt ]; then
    echo "PyQt detected!"
else
    pip install -r requirements.txt
fi

LAUNCH_TEST=$(which launch_browser.sh)

if [ -z $LAUNCH_TEST ]; then
    mkdir /usr/local/bin/browser
    cp launch_browser.sh /usr/local/bin/
    cp browser.py /usr/local/bin/browser/
    cp -R venv /usr/local/bin/browser/
    chown -R browser:browser /usr/local/bin/browser
    chown browser:browser /usr/local/bin/launch_browser.sh
    chmod -R 775 /usr/local/bin/browser
    chmod -R g+s /usr/local/bin/browser
    chmod a+rx /usr/local/bin/launch_browser.sh
    chmod g+s /usr/local/bin/launch_browser.sh
else
    echo "Browser is already installed!"
fi

