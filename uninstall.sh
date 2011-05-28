#!/bin/bash

PREFIX="/usr/local"

INSTALLDIR="$PREFIX/share/coffeebreak"
BINDIR="$PREFIX/bin"


# Are we root?
if [[ $EUID -ne 0 ]]; then
    echo "You must be root to run this script." 2>&1
    exit 1
else
	
	rm -r $INSTALLDIR
	rm $BINDIR/coffeebreak

	echo "CoffeeBreak has been successfully uninstalled."
	
fi
