# Flask Application CI/CD using Heroku and Travic CI

[![Build Status](https://travis-ci.com/aliartiza75/flask-cicd-using-travis-heroku.svg?branch=master)](https://travis-ci.com/aliartiza75/flask-cicd-using-travis-heroku)

## Overview

This repository contains code for get name api endpoints.

### Install Packages

1. Install python 3.7.

2. Install pip3
```bash
sudo apt install python3-pip
```
3. Install packages:
```bash
sudo pip3 install -r requirements.txt
```


### Configure Application With Travis CI for CI pipeline.

A file `.travisyml` exists that contains configuration for the CI pipeline. Once travis ci is configured to use this application, the pipeline will be trigerred automatically.

### Deploy Application Locally

1.1. Deploy application locally:

```bash
python3 app.py
```

**NOTE**
In the `app.py` file the default port is `5000` because flask server uses it(not manditory). If you want to change the port just change it in the `app.py` file and run the comamnd given above. 

If you use flask run command it will not use the port specified in the `app.py` file. So to change the port run the command given below:

```bash
flask run -p <5121>
```

2. List of endpoints:
```bash
# endpoint to get the webpage
http://localhost:5000/


# endpoint to get the json response
http://localhost:5000/message?name=Irtiza
```

1.2. Application is deploy on heroku on this [link](https://irtiza-get-name.herokuapp.com/)
```bash
# endpoint to get the webpage
https://irtiza-get-name.herokuapp.com/

# endpoint to get the json response, either open in a browser or use cli
https://irtiza-get-name.herokuapp.com/message?name=Irtiza
```

### Deploy Application on Heroku

1. Create virtual env:

```bash
python3 -m venv venv/
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

3. Install packages:
```bash
pip3 install -r requirements.txt
```

4. Create a Procfile, it is already created. This file tells heroku to run a commands. The web command tells Heroku to start a web server for the application, using gunicorn. Application is called app.py, therfore app name has been set as `app`.

5. Configure heroku repository:
```bash
heroku create flask-cicd-using-travis-heroku
```

6. Push your code to the repository:
```bash
git push heroku master
```

It will output the application url

### Testing

1. To the the linting:

```bash
./pycheck
```

2. To test the code:

```bash
# Make sure server is running locally before executing the command below
python3 test_datetime_service.py
```