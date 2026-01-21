#!/bin/sh

# Ensure dependencies
pyqt5_check=$(dpkg -l | grep python3-pyqt5)
pyqt5web_check=$(dpkg -l | grep python3-pyqt5.qtwebengine)

if [ -z "$pyqt5_check" ]; then
    echo "Installing pyqt5..."
    apt-get install -y python3-pyqt5
fi

if [ -z "$pyqt5web_check" ]; then
    echo "Installing pyqt5 web-engine..."
    apt-get install -y python3-pyqt5.qtwebengine
fi

# Install files
if [ ! -d /usr/local/lib/barrel ]; then
    echo "Creating local folder"
    mkdir /usr/local/lib/barrel
fi

if [ ! -e /usr/local/bin/run_browser.sh ]; then
	echo "Copying run script..."
	cp ./run_browser.sh /usr/local/bin/ 
fi

if [ ! -e /usr/local/lib/barrel/magic.py ]; then
    cp ./magic.py /usr/local/lib/barrel/
fi

if [ ! -e /usr/local/lib/barrel/barrel.py ]; then
	cp ./barrel.py /usr/local/lib/barrel/
fi

if [ ! -e /usr/local/lib/barrel/barrel.payload ]; then
	echo "Creating encoded browser payload..."
	./obfuscate.py
fi
