# Home Dashboard

A digital clock and weather app built with Python for the Raspberry Pi

Check out the documentation to get started:
https://aalcala07.github.io/home_dashboard/


## Developer Instructions

These instructions are for anyone wanting to change the source code.

### Initial Environment Setup

1. Create venv from within project directory:

```
python -m venv venv
source venv/bin/activate
```

2. Install packages:

```
pip install -r requirements.txt
```

3. Copy `.env.example`

```
cp .env.example .env
```

4. Edit config values as needed

### Starting and Stopping Environment

To start the venv use:

```
source venv/bin/activate
```

To exit the venv use:

```
deactivate
```

### Launching the App

Run the script inside of your project directory (make sure venv is activated):

```
python main.py
```

### Saving Requirements

If you install any new packages using pip, save them to the requirements so they are added when setting up a new environment.

```
pip freeze > requirements.txt
```