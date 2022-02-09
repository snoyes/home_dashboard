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

## Development

### Save Requirements

If you install any new packages using pip, save them to the requirements so they are added when setting up a new environment.

```
pip freeze > requirements.txt
```

## Deploying to Raspberry Pi

1. Create deploy key, add to repo
2. Clone repo
3. Install venv

```
sudo apt-get install python3-venv
```

4. Create venv and activate

```
cd home_dashboard
python3 -m venv venv
source venv/bin/activate
```

5. Install packages

```
pip install -r requirements.txt
```

6. Copy example config

```
cp .env.example .env
```

7. Update config with API key and other settings
8. Launch app
```
python main.py
```