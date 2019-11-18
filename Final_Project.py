
import requests, json, time, urllib2
import pandas as pd

def city_main(_city_name):
    api_key = ""
    base_url = " "
    complete_url = base_url + "appid=" + api_key + '&mode=json&units=imperial'+"&q=" + _city_name
    api_on(complete_url)
    response = requests.get(complete_url)
    x = response.json()
    json_handler(x)

#This is for if a zip code is the perferred input
def zip_main(_zip_name):
    api_key = ""
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + '&mode=json&units=imperial'+"&zip=" + _zip_name
    api_on(complete_url)
    response = requests.get(complete_url)
    x = response.json()
    json_handler(x)

def json_handler(x):
    print('Location: Lon {}, Lat{}'.format(x['coord']['lon'],x['coord']['lat']))
    print('In {}, {} the temperature is {} degrees Ferieheit with {}'.format(x['name'],x['sys']['country'],x['main']['temp'],x['weather'][0]['main']))
    print('For today this is a MAX temperature of {} degrees Ferieheit and a MIN Temperature of {} degrees Ferieheit'.format(x['main']['temp_max'],x['main']['temp_min']))
    print('The following are other readings from today:')
    print('\t Humidity: {}'.format(x['main']['humidity']))
    print('\t Pressure: {}'.format(x['main']['pressure']))
    print('\t Sunrise: {}'.format(time.ctime(x['sys']['sunrise'])))
    print('\t Sunset: {}'.format(time.ctime(x['sys']['sunset'])))
    print('\t Wind: {}mph'.format(x['wind']['speed']))
    print('\t Wind Deg: {} degrees'.format(x['wind']['deg']))

    dfALL = pd.DataFrame({"ALL":[]})

    df.append({"ADD":[x['coord']['lon'], x['coord']['lat'], x['name'] , x['sys']['country'],
                                 x['main']['temp'], x['weather'][0]['main'],x['main']['temp_max'],
                                 x['main']['temp_min'],x['main']['humidity'],x['main']['pressure'],
                                 x['sys']['sunrise'], x['sys']['sunset'], x['wind']['speed'],
                                 x['wind']['deg']]})

    print(dfALL)

#to check if the website is up by seeing if it a valid address
#checks if the city or zip code is valid
def api_on(complete_url):
    try:
        urllib2.urlopen(complete_url, timeout=1)
        return True
    except urllib2.URLError as err:
        print('The URL you are trying to reach is not valid. Please check your connection. Or check your input.')
        return False

#main function to run all the code
def main():
    print("Hello time to get the weather.")
    try:
        done = False
        #to loop through the program until the done option is selected
        while done != True:
            _user_choice = raw_input("Would you like to enter a ZIP or City? Or enter done.  ").lower()

            #will run the city_main function is condition is met
            if _user_choice == 'city':
                _city_name = raw_input("Enter city name:  ").lower()
                city_main(_city_name)
                continue
            #will run the zip_main function is condition is met
            elif _user_choice == 'zip':
                _zip_name = raw_input("Enter ZIP code:  ").lower()
                zip_main(_zip_name)
                continue
            #will quit the program if selected
            elif _user_choice == 'done':
                done = True
            #IF you try to break my input
            else:
                print('Type in city or zip. Or enter in done to quit.')

    except:
        pass

main()
