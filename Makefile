#https://makefiletutorial.com/

.PHONY: info
info:
	echo "\nList of Makefile commands:\n" && echo "  readme" && echo "  run"  && echo "  screenshots-root" && echo "  screenshots"  && echo "  github"   && echo "  simulator" 
info-info:
	echo "\noutput the list of commands for this Makefile\n"

.PHONY: readme
readme:
	echo "commit Readme file"
	git commit -am 'readme'
	echo "publish it on github on Master branch"
	git push -u origin master
info-readme:
	echo "\nCommit the Readme file and push this repository on Github\n"


.PHONY: setup
setup:
	poetry install -v
	poetry run python sp_ask_service_availability_alert.py
info-setup:
	echo "\nRun this python app\n"


.PHONY: run
run:
	poetry run python sp_ask_service_availability_alert.py
info-run:
	echo "\nRun this python app\n"

.PHONY: packages
packages:
	poetry install
info-packages:
	echo "\nInstall packages\n"

.PHONY: github
github:
	echo "--On Mac Open this github repository url--"
	open https://github.com/guinslym/sp_ask_presence_alert
info-github:
	echo "\nOpen this github repository url \n"

.PHONY: push
push:
	git push -u origin master
info-push:
	echo "\nGit Pushed to master branch repository\n"