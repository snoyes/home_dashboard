## Setup Environment

Create venv from within project directory:

```
python -m venv venv
source venv/bin/activate
```

Install packages:

```
pip install -r requirements.txt
```

## Start Environment

Start your venv:

```
source venv/bin/activate
```

## Exit Environment

```
deactivate
```

## Run App

Run the script inside of your project directory (make sure venv is activated):

```
python main.py
```

## Save Requirements

If you install any new packages using pip, save them to the requirements so they are added when setting up a new environment.

```
pip freeze > requirements.txt
```