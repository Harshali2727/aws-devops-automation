# AWS DevOps Automation Project

## Overview

A beginner-friendly DevOps project demonstrating a Python HTTP application, automated unit testing, and Continuous Integration (CI) using GitHub Actions.

## Technologies

- Python 3.12

- Git and GitHub

- GitHub Actions

- Windows and Ubuntu

## Project Structure

```text

aws-devops-automation/
├── app/
│   └── app.py
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md

```

## Features

- Python HTTP application

- Health-check endpoint at `/health`

- Automated unit tests

- GitHub Actions CI pipeline

- Automatic tests on pushes and pull requests targeting `main`

## Run Locally

From the project root, run:

```bash

python app/app.py

```

Open this URL in your browser:

`http://127.0.0.1:8000/health`

Expected response:

```json

{"status": "healthy", "project": "AWS DevOps Automation"}

```

## Run Tests

Run this command from the project root:

```bash

python -m unittest discover -s tests -v

```

## Continuous Integration

The workflow at `.github/workflows/ci.yml` automatically runs the Python tests using GitHub Actions.

## Future Improvements

- Add code-quality checks

- Containerize the application with Docker

- Explore cost-controlled AWS deployment

- Extend deployment automation

## Author

AWS Cloud & DevOps Learner
