import urllib2
import re
from bs4 import BeautifulSoup

site='https://www.worldweatheronline.com/melbourne-weather-text/victoria/au.aspx'
page = urllib2.urlopen(site)
soup = BeautifulSoup(page, "lxml")

temp = soup.find("div", class_="report_text temperature")
temp = str(temp)
temp = re.findall(r"\-?\d+", temp)

skies = soup.find("div", class_="report_text light_text")
skies = str(skies.string)

wind = soup.find("div", class_="col-md-7 col-xs-6")
wind = str(wind)
start = wind.find("Wind")+6
end = start+2
wind=wind[start:end]

text = soup.find("div", class_="weather_forecastdiv marbot")
text = str(text.find("p"))
text = BeautifulSoup(text, "lxml").text


print "Short forecast: ", skies
print "Temperature (Celsius): ", temp[0]
print "Wind speed (mph): ", wind
print "Long forecast: ", text
