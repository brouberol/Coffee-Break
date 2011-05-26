#!/bin/bash

PREFIX="/usr/local"

INSTALLDIR="$PREFIX/share/coffeebreak"
BINDIR="$PREFIX/bin"


# Are we root?
if [[ $EUID -ne 0 ]]; then
    echo "You must be root to run this script." 2>&1
    exit 1
else
    mkdir -p "$INSTALLDIR"
    cp *.{png,py} "$INSTALLDIR/"
    ln -s "$INSTALLDIR/CoffeeBreak.py" "$BINDIR/coffeebreak"
    chmod +x "$BINDIR/coffeebreak"

    echo "CoffeeBreak bin located in $BINDIR/coffeebreak directory"
    echo "Command is 'coffeebreak'"
fi
