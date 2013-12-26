import urllib2
import json
import sys

# WARNING: grabbing weather data from OpenWeatherMap is slow. Use this class sparingly!

# define a class called WeatherData
class WeatherData:

    # the request URL
    url = "http://api.openweathermap.org/data/2.5/weather";

    # constructor that accepts latitude and longitude and gets weather data
    def __init__(self, latitude, longitude):
        
        # check that both latitude and longitude are passed in as floats
        latitude = float(latitude)
        longtitude = float(longitude)

        # perform the GET and store result
        result = urllib2.urlopen(WeatherData.url+"?lat="+str(latitude)+"&lon="+str(longitude)).read()
        
        # parse the JSON result
        self.data = json.loads(result)

        # get relevant data from JSON string. If data item cannot be found, set it to 'None'        
        try:
            self.cloud_cover = self.data["clouds"]["all"]; 
        except KeyError:
            self.cloud_cover = None

        try:    
            self.temperature = self.data["main"]["temp"]
        except KeyError:
            self.temperature = None
    
        try:
            self.humidity = self.data["main"]["humidity"]
        except KeyError:
            self.humidity = None
    
    # function to return cloud cover data
    def getCloudCover(self):

        return self.cloud_cover

    # function to return temperature data. Temperature data is returned in Kelvib
    def getTemperature(self):

        return self.temperature

    # function to return humidity data, Humidity data is return as a percentage
    def getHumidity(self):

        return self.humidity

    # function to return all JSON data
    def getAllJSONData(self):

        return self.data
