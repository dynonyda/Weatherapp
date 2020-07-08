import requests


def main():

    print_header()
    city = input('What city do you want the weather information? ')
    key = getLoc(city)
    getForecast(key, city)


def print_header():

    print("-----------------------------------")
    print("       Weather Forecast APP")
    print("-----------------------------------")
    print()

def getLoc(city):
    url = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=oSiVGZ7dpRMKj7htAbxAXlTnGmSD7yU6&q={}&details=true&offset=0".format(city)
    rqs = requests.get(url)
    data = rqs.json()
    locKey = data[0]['Key']

    return locKey


def getForecast(key, city):
    urf = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/{}?apikey=oSiVGZ7dpRMKj7htAbxAXlTnGmSD7yU6&details=true&metric=true".format(key)
    res = requests.get(urf)
    data = res.json()

    for cuaca1 in data['DailyForecasts']:
        print("Weather Forecast for {} in ".format(city.upper().strip()) + cuaca1['Date'])
        print("Min Temp         :"+ str(cuaca1['Temperature']['Minimum']['Value'])+ "°C")
        print("Max Temp         :"+ str(cuaca1['Temperature']['Maximum']['Value'])+ "°C")
        print("Day Forecast     :"+ str(cuaca1['Day']['ShortPhrase']))
        print("Night Forecast   :"+ str(cuaca1['Night']['ShortPhrase']))
        print("------------------------------------------------------------------------------")

if __name__ == '__main__':

    main()