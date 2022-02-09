import requests, json
from os.path import exists
from decouple import config

OPEN_WEATHER_MAP_API_KEY = config('OPEN_WEATHER_MAP_API_KEY', default='', cast=str)
OPEN_WEATHER_MAP_API_URL = "https://api.openweathermap.org"
LOCATION_LAT = config('LOCATION_LAT', cast=float)
LOCATION_LONG = config('LOCATION_LONG', cast=float)
FREQUENCY = config('WEATHER_RELOAD_FREQUENCY_MINUTES', default=5, cast=int)

# Request data from API
def fetch():

    if not OPEN_WEATHER_MAP_API_KEY or OPEN_WEATHER_MAP_API_KEY == '':
        print('Error: Cannot fetch weather, missing OPEN_WEATHER_MAP_API_KEY')
        return

    print('Fetching weather')

    try:
        r = requests.get(f'{OPEN_WEATHER_MAP_API_URL}/data/2.5/onecall?lat={LOCATION_LAT}&lon={LOCATION_LONG}&appid={OPEN_WEATHER_MAP_API_KEY}&exclude=minutely,hourly,alerts&units=imperial')
    except:
        print('Error: unable to retrieve weather data')
    else:
        weather_data = r.json()
        weather_data_file = open(".weather_data", "w") 
        weather_data_file.write(json.dumps(weather_data, indent = 4))
        weather_data_file.close()
        print('Weather data saved')

# Get data from cache file
def get():

    if(exists('.weather_data') == False):
        return None
        
    with open('.weather_data') as json_file:
        weather_data = json.load(json_file)

    return weather_data

# Get the current weather
def current():

    data = get()

    if not data:
        return None

    return data['current']

# Get the daily forecast
def daily():

    data = get()

    if not data:
        return None

    return data['daily']