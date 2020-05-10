# get-name API

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

### 1. Deploy Application Locally

1.1. Deploy application locally:

```bash
python3 app.py
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