# selenium-python-pom-example

Example of selenium test using Page-Object-Model running on pytest framework.
This example currently supports Linux distribution or Windows with Chrome browser of version 66-68 installed.
Surprisingly it was also tested successfully on Chrome 81 as well.

To run on Windows, just install the package requirements and launch the test:
```
pip install -r requirements\requirements.txt
pytest
``` 

To run on Linux, make the chromedriver file executable by running the following command from root project dir:
```
chmod +x driver/executable/chromedriver
```

Install the requirements:
```
# Ubuntu:
sudo apt install python-pytest python-pip
pip install -r requirements/requirements.txt

# Fedora:
sudo apt install python-pytest python-pip
pip install -r requirements/requirements.txt
```

Then in order to run the test (with log output):
```
pytest -s
```
