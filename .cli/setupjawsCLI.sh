#!/usr/bin/env bash

source $PWD"/venv/bin/activate"
echo which python
echo python --version
select var in run_tests run_sanity
do
	case $var in
		run_tests)
 			echo "---All test started---"
			# call python file
			python "./startTest.py"
			break
 		;;
		run_sanity)
			echo "---sanity test started---"
			python "./startTest.py"
			break
			# call python file with argument
		;;
		*)
			echo "please select the proper option from above"
			echo " try:  jawsui "
			break
		esac
	done
deactivate

#if [[ "$1" != "--help" && "$1" != "run" ]]; then
#	echo "try jawsui --help for more info..\n run test: for full test"
#	echo "run sanity: for sanity test"

