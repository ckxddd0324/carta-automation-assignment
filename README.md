# carta-automation-assignment


### ⚠️ Requirement
- Please at least have python 3 or docker installed locally

## How to generate the report with Docker (Report.html)
    1. git clone/download as zip
    2. go to the directory
    3. go to tests folder
    4. rename ".env_sample" to ".env"
    5. add your own openweathermap api key to ".env" (.env file should be something like API_KEY=SOME_RANDOM_HASH)
    6. go to the directory(/carta-automation-assignment), run "./run_test.sh"
    7. Vola! Now you should see a new file Report.html
    

## Without docker? 
### Prerequisite
```
- Python3
- python virtual environment setup [https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/]
```
    1. git clone/download as zip
    2. go to the directory
    3. cd into tests folder
    3. go to tests folder
    4. rename ".env_sample" to ".env"
    5. add your own openweathermap api key to ".env" (.env file should be something like API_KEY=SOME_RANDOM_HASH)
    6. create python virtual environment with "python3 -m venv venv" 
    7. activate the virtual environemnt with "source venv/bin/activate"
    8. run "pip install -r requirements.txt" to install pacakage
    9. run "pytest -s --html=report.html --self-contained-html", this would generate a report.html in tests folder for test reporting
    
## Attachment
I have also included the result I have generated locally, the file is located in `/result` direcotory
