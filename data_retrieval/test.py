import urllib2
from bs4 import BeautifulSoup

london='https://www.worldweatheronline.com/london-weather-text/city-of-london-greater-london/gb.aspx'
london_page = urllib2.urlopen(london)
london_soup = BeautifulSoup(london_page, "lxml")

new_york='https://www.worldweatheronline.com/new-york-weather-text/new-york/us.aspx'
new_york_page = urllib2.urlopen(new_york)
new_york_soup = BeautifulSoup(new_york_page, "lxml")

san_fran='https://www.worldweatheronline.com/san-francisco-weather-text/california/us.aspx'
san_fran_page = urllib2.urlopen(san_fran)
san_fran_soup = BeautifulSoup(san_fran_page, "lxml")

toronto='https://www.worldweatheronline.com/toronto-weather-text/ontario/ca.aspx'
toronto_page = urllib2.urlopen(toronto)
toronto_soup = BeautifulSoup(toronto_page, "lxml")

rio='https://www.worldweatheronline.com/rio-weather-text/rio-de-janeiro/br.aspx'
rio_page = urllib2.urlopen(rio)
rio_soup = BeautifulSoup(rio_page, "lxml")

miami='https://www.worldweatheronline.com/miami-weather-text/florida/us.aspx'
miami_page = urllib2.urlopen(miami)
miami_soup = BeautifulSoup(miami_page, "lxml")

moscow='https://www.worldweatheronline.com/moscow-weather-text/moscow-city/ru.aspx'
moscow_page = urllib2.urlopen(moscow)
moscow_soup = BeautifulSoup(moscow_page, "lxml")

trondheim='https://www.worldweatheronline.com/trondheim-weather-text/sor-trondelag/no.aspx'
trondheim_page = urllib2.urlopen(trondheim)
trondheim_soup = BeautifulSoup(trondheim_page, "lxml")

melbourne='https://www.worldweatheronline.com/melbourne-weather-text/victoria/au.aspx'
melbourne_page = urllib2.urlopen(melbourne)
melbourne_soup = BeautifulSoup(melbourne_page, "lxml")

import re

rio_temp = rio_soup.find("div", class_="report_text temperature")
rio_temp = str(rio_temp)
rio_temp = re.findall(r"\-?\d+", rio_temp)

rio_skies = rio_soup.find("div", class_="report_text light_text")
rio_skies = str(rio_skies.string)

rio_wind = rio_soup.find("div", class_="col-md-7 col-xs-6")
rio_wind = str(rio_wind)
start = rio_wind.find("Wind")+6
end = start+2
rio_wind=rio_wind[start:end]

rio_text = rio_soup.find("div", class_="weather_forecastdiv marbot")
rio_text = str(rio_text.find("p"))
rio_text = BeautifulSoup(rio_text, "lxml").text



print "Short forecast: ", rio_skies
print "Temperature (Celsius): ", rio_temp[0]
print "Wind speed (mph): ", rio_wind
print "Long forecast: ", rio_text
