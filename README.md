﻿# Fast API Address Mapper

## Setup Instructions

### Python Version

```bash
Python 3.9
```

### Downlaod/Clone Repository

```bash
git clone git@github.com:jaywelj/fastapi-address-mapper.git
```

### Install Required Python Modules

```bash
cd fastapi-address-mapper
pip install -r address-app/requirements.txt
```
note: activate a virtual environment before installing requirements
### Start Web Server

To start the web server you need to run the following sequence of commands.

First cd into your desired tutorial folder.
```bash 
cd fastapi-address-mapper
```
Next run the django web server.
```bash
uvicorn address-app.main:app --reload
```
Open Swagger UI from your browser to test out the API

```buildoutcfg
http://127.0.0.1:8000/docs
```
