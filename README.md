# selenium-python-pom-example

Example of selenium test using Page-Object-Model running on pytest framework.
This example currently supports Linux distribution with Chrome browser of version 66-68 installed.

To run on Linux, make the chromedriver file executable by running the following command from root project dir:
```
chmod +x executable/chromedriver
```

Install the requirements:
```
pip install -r requirements/requirements.txt
```

Then in order to run the test (with log output):
```
pytest -s
```
