#!/usr/bin/env bash

# check python3
echo "verifying python3 version"
pyv="$(python3 -V 2>&1)"
if [[ $pyv =~ Python.* ]]
then
	echo "python3 is available"
else
	echo "python3 not available.."
	apt-get -Y install python3
fi

# check pip for python3
echo "verifying pip3 versionfor python3 ..."
pipv="$(pip3 -V 2>&1)"
if [[ $pipv =~ pip.* ]]
then
        echo "pip for python3 is available"
else
        echo "pip for python3 not available.."
        echo "pip installation started .."
fi

# verifying VENV version
echo "verifying vertualenv version.."
VENV="$(pip3 list | grep virtualenv 2>&1)"
if [[ $VENV =~ virtualenv.* ]]
then
	echo "virtualenv available.."
else
	echo "virtualenv installation started.."
fi

# verify VEW
VEW="$(pip3 list | grep virtualenvwrapper 2>&1)"
if [[ $VEW =~ virtualenvwrapper.* ]]
then
	echo "virtualenvwrapper is available.."
else
	echo "virtualenvwrapper instllation started.."
	pip3 install virtualenvwrapper
	PID=$!
	wait $PID || { echo "error in virtualenvwrapper installation" >&2; exit 1; }
	echo "virtualenvwrapper instllationcompleted"
fi

#export WORKON_HOME=~/Envs
export WORKON_HOME=$PWD && source /usr/local/bin/virtualenvwrapper.sh && mkvirtualenv --python=python3 venv

export JAWS_CLI=$PWD"/.cli" && export PATH=$PATH:$JAWS_CLI

alias jawsui="setupjawsCLI.sh"

#echo "$pyv"
#echo "$pipv"
#echo "$VENV"
#echo "$VEW"
