import requests


def main():
    print_header()
    while True:
        city = ""
        Loc=cekcharnum(city)
        key=getLoc(Loc)
        if key == "1":
            print("City Not Found, Please re-Input the city!")
            print("")
        elif key == "2":
            print("Check Your Internet Connection!!!")    
            print("")
        else:
            break

    getForecast(key,Loc)



def print_header():

    print("-----------------------------------")
    print("       Weather Forecast APP")
    print("-----------------------------------")
    print()


def cekcharnum(masuk):
    while True:
        masuk = input("Where city you want to know? ")
        if "1" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "2" in masuk:
            print("Don't input a number and or Special Character!!")    
        elif "3" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "4" in masuk:
            print("Don't input a number and or Special Character!!") 
        elif "5" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "6" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "7" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "8" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "9" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "0" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "!" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "@" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "#" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "$" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "%" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "^" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "&" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "*" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "(" in masuk:
            print("Don't input a number and or Special Character!!")
        elif ")" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "-" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "_" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "=" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "+" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "[" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "]" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "|" in masuk:
            print("Don't input a number and or Special Character!!")
        elif ":" in masuk:
            print("Don't input a number and or Special Character!!")
        elif ";" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "'" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "<" in masuk:
            print("Don't input a number and or Special Character!!")
        elif ">" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "," in masuk:
            print("Don't input a number and or Special Character!!")
        elif "." in masuk:
            print("Don't input a number and or Special Character!!")
        elif "/" in masuk:
            print("Don't input a number and or Special Character!!")
        elif "?" in masuk:
            print("Don't input a number and or Special Character!!")
        else:
            break    
    return masuk



def getLoc(city):
    url = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=oSiVGZ7dpRMKj7htAbxAXlTnGmSD7yU6&q={}&details=true&offset=0".format(city)
    rqs = requests.get(url)
    resp = rqs.status_code
    if resp == 200:    
        data = rqs.json()    
        if len(data)>1:
            print("Please choose and copy the key from this list:")
            print()
            for kode in data:
                print("Region: "+ str(kode['Region']['EnglishName']))
                print("Country: "+ str(kode['Country']['EnglishName']))
                print("Province: "+ str(kode['AdministrativeArea']['EnglishName']))
                print("District: "+ str(kode['SupplementalAdminAreas'][0]['EnglishName']))
                print("Sub-District: "+ str(kode['SupplementalAdminAreas'][1]['EnglishName']))
                print("Location Key: "+ str(kode['Key']))
                print("-------------------------------------")

            print()
            locKey = input("Paste here the key: ")    

            return locKey

        elif len(data)==1:
            locKey = data[0]['Key']

            return locKey

        else:
            Fail="1"
            return Fail 
            
    else:
        Fail2="2"
        return Fail2



def getForecast(key, city):
    urf = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/{}?apikey=oSiVGZ7dpRMKj7htAbxAXlTnGmSD7yU6&details=true&metric=true".format(key)
    res = requests.get(urf)
    data = res.json()
    print("------------------------------------------------------------------------------")

    for cuaca1 in data['DailyForecasts']:
        print("Weather Forecast for {} in ".format(city.upper().strip()) + cuaca1['Date'])
        print("Min Temp         :"+ str(cuaca1['Temperature']['Minimum']['Value'])+ "°C")
        print("Max Temp         :"+ str(cuaca1['Temperature']['Maximum']['Value'])+ "°C")
        print("Day Forecast     :"+ str(cuaca1['Day']['ShortPhrase']))
        print("Night Forecast   :"+ str(cuaca1['Night']['ShortPhrase']))
        print("------------------------------------------------------------------------------")

if __name__ == '__main__':

    main()
