# sample script that uses the weather data class

# import the WeatherData class
from weather_data import WeatherData

# create two new variables to hold latitude and longitude
latitude = 76.382
longitude = 163.87

# create a new WeatherData object and pass latitide and longitude into constructor
data = WeatherData(latitude, longitude)

# get relevant data from class
temperature = data.getTemperature() # WARNING: temperature is reported in Kelvin
cloud_cover = data.getCloudCover() # cloud cover is reported as a percentage
humidity = data.getHumidity() # humidity is reported as a percentage

# print out data
print temperature, cloud_cover, humidity
