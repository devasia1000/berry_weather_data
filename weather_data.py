import urllib2
import json

# WARNING: this class is slow. Use sparingly!

# define a class called WeatherData
class WeatherData:

    # the request URL
    url = "http://api.openweathermap.org/data/2.5/weather";

    # constructor that accepts latitude and longitude and prints out weather data
    def __init__(self, latitude, longitude):
    
        # check that both latitude and longitude are passed in as floats
        latitude = float(latitude)
        longtitude = float(longitude)

        # perform the GET and store result
        result = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?lat="+str(latitude)+"&lon="+str(longitude)).read()
        
        # print out result
        print result

        # parse the JSON result
        data = json.loads(result)

        # get relevant data from JSON string
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"];

        print temperature, humidity

# used to test our class        
weather_data = WeatherData(12.3, 56.32)
