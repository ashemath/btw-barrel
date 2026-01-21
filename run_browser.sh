#!/bin/sh

APP=$(python3 /usr/local/lib/barrel/barrel.py | python3 - 2>&1 /dev/null)&
