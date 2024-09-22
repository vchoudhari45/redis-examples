# Redis Examples 

This repository contains a collection of examples from Redis University course.

## Create a virtual environment and activate it (optional but recommended).
```sh
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies
```sh
pip install -r requirements.txt -r test_requirements.txt
```

## Run Tests Using unittest
```sh
tox
```

## Build and Run Container Locally

```sh
docker compose up --build
```
