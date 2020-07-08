import requests
import bs4
import collections

def main():
    print_header()
    state = input('What state do you want the weather for (e.g. Texas, )? ')
    city = input('What city do you want the weather for (e.g. Jakarta, Surabaya)? ')
    html = get_html_from_web(state, city)
    print (html)
    #report = get_weather_from_html(html)

    #print('The temp in {} is {} {} and {}.'.format(
        #report.loc,
        #report.temp,
        #report.scale,
        #report.cond
    #))

def print_header():
    print('---------------------------------')
    print('   ALDINO & STEVEN WEATHER APP')
    print('---------------------------------')
    print()

def get_html_from_web(state, city):
    url = 'https://www.wunderground.com/weather/us/{}/{}'.format(state.lower().strip(), city.lower().strip())
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    main()