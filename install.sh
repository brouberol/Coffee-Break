#!/bin/bash

PREFIX="/usr/local"

INSTALLDIR="$PREFIX/share/coffeebreak"
BINDIR="$PREFIX/bin"


# Are we root?
if [[ $EUID -ne 0 ]]; then
    echo "You must be root to run this script." 2>&1
    exit 1
else
	dpkg -l | grep pygame >/dev/null

	if [ $? -ne 0 ]; then # if pygame not installed
		echo "It appears that python-pygame is not installed. Would you like to install it? [y/n]"
		read ans

		if [ $ans = "y" ]; then  #user willing to install
			apt-get install python-pygame

			mkdir -p "$INSTALLDIR"
			cp *.{png,py,ogg} "$INSTALLDIR/"
			ln -s "$INSTALLDIR/CoffeeBreak.py" "$BINDIR/coffeebreak"
			chmod +x "$BINDIR/coffeebreak"

			echo -e "CoffeeBreak bin file located in $BINDIR/coffeebreak directory\n"
			echo "Command is 'coffeebreak X' where X is optional and represents the break duration (min)."
			echo "Default : X = 10"

		else
			echo "Aborting..."
			exit 1
		fi
			
	else
		mkdir -p "$INSTALLDIR"
		cp *.{png,py,ogg} "$INSTALLDIR/"
		ln -s "$INSTALLDIR/CoffeeBreak.py" "$BINDIR/coffeebreak"
		chmod +x "$BINDIR/coffeebreak"
	
		echo -e "CoffeeBreak bin file located in $BINDIR/coffeebreak directory\n"
		echo "Command is 'coffeebreak X' where X is optional and represents the break duration (min)."
		echo "Default : X = 10"
	fi

fi
