#! /usr/bin/bash

HelpMenu()
{
	echo "This script is meant to automate the commit process"
	echo
	echo "usage: ./Auto-Commit.sh [-m | -h]"
	echo "option:"
	echo "[REQUIRED]	m	The commit message"
	echo "		h	Display this help menu"
}

Commit()
{
	echo "Staging all changes"
	git add .
	echo "All changes staged"
	git status
	git commit -m $message
	git status
	git push
}

while getopts ":hm:" option; do
	case $option in
		h) # Display help menu
			HelpMenu
			exit;;
		m) # The commit message
			message=$OPTARG
			Commit;;
		\?) # Invalid option
			echo "ERROR: Invalid option"
			exit;;
	esac
done
