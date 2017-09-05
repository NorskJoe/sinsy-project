# -*- coding: utf-8 -*-
from urllib import urlencode
import urllib2
from lxml import etree
from lxml import objectify

FREE_API_KEY = ""
PREMIUM_API_KEY = ""

_keytype = "free"
_key = FREE_API_KEY

def internet_on():
    """fast test by trying one of google IPs"""
    try:
        #unfortunately sometimes google is unstable in China
        urllib2.urlopen('http://www.baidu.com',timeout=3)
        return True
    except urllib2.URLError:
        try:
            urllib2.urlopen('http://www.google.com',timeout=3)
            return True
        except urllib2.URLError:
            return False

def setKeyType(keytype="free"):
    """ keytype either "free" or "premium", set the key if it exists"""
    global _key, _keytype, FREE_API_KEY, PREMIUM_API_KEY

    keytype = keytype.lower()
    if keytype in ("f", "fr", "free"):
        _keytype = "free"
        if FREE_API_KEY == "":
            print "Please set FREE_API_KEY"
            return False
        else:
            _key = FREE_API_KEY
            return True
    elif keytype.startswith("prem") or keytype in ("nonfree", "non-free"):
        _keytype = "premium"
        if PREMIUM_API_KEY == "":
            print "Please set PREMIUM_API_KEY"
            return False
        else:
            _key = PREMIUM_API_KEY
            return True
    else:
        print "invalid keytype", keytype
        return False

def setKey(key, keytype):
    """ if keytype is valid, save a copy of key accordingly
        and check if the key is valid """
    global _key, _keytype, FREE_API_KEY, PREMIUM_API_KEY

    keytype = keytype.lower()
    if keytype in ("f", "fr", "free"):
        keytype = "free"
        FREE_API_KEY = key
    elif keytype.startswith("prem") or keytype in ("nonfree", "non-free"):
        keytype = "premium"
        PREMIUM_API_KEY = key
    else:
        print "invalid keytype", keytype
        return

    oldkey = _key
    oldkeytype = _keytype
    _key = key
    _keytype = keytype

    w = LocalWeather("london")
    # w.data != False rather than w.data to suppress Python 2.7 FurtureWarning:
    # "The behavior of this method will change in future versions...."
    if w is not None and hasattr(w, 'data') and w.data != False:
        return True
    else:
        print "The key is not valid."
        _key = oldkey
        _keytype = oldkeytype
        return False

class WWOAPI(object):
    """ The generic API interface """
    def __init__(self, q, **keywords):
        """ query keyword is always required for all APIs """
        if _key == "":
            print "Please set key using setKey(key, keytype)"
        else:
            if internet_on():
                self.setApiEndPoint(_keytype == "free")
                self._callAPI(q=q, key=_key, **keywords)
            else:
                print "Internet connection not available."

    def setApiEndPoint(self, freeAPI):
        if freeAPI:
            self.apiEndPoint = self.FREE_API_ENDPOINT
        else:
            self.apiEndPoint = self.PREMIUM_API_ENDPOINT

    def _callAPI(self, **keywords):
        for arg in keywords:
            if keywords[arg] != None:
                if keywords[arg] in ("No", "NO", "None"):
                    keywords[arg] = "no"
                elif keywords[arg] in ("Yes", "YES", "Yeah"):
                    keywords[arg] = "yes"
            else:
                del keywords[arg]

        url = self.apiEndPoint + "?" + urlencode(keywords)
        try:
            response = urllib2.urlopen(url).read()
        except urllib2.URLError:
            print "something wrong with the API server"
            return

        # if the key is invalid it redirects to another web page
        if response.startswith("<?xml "):
            self.data = objectify.fromstring(response)
            if self.data is not None and hasattr(self.data, 'error') and self.data.error != False:
                print self.data.error.msg
                self.data = False
        else:
            self.data = False

class LocalWeather(WWOAPI):
    FREE_API_ENDPOINT = "http://api.worldweatheronline.com/free/v1/weather.ashx"
    PREMIUM_API_ENDPOINT = "http://api.worldweatheronline.com/premium/v1/premium-weather-V2.ashx"

    def __init__(self, q, num_of_days=1, **keywords):
        """ q and num_of_days are required. max 7 days for free and 15 days for premium """
        super(LocalWeather, self).__init__(
            q, num_of_days=num_of_days, **keywords)

class LocationSearch(WWOAPI):
    FREE_API_ENDPOINT = "http://api.worldweatheronline.com/free/v1/search.ashx"
    PREMIUM_API_ENDPOINT = "http://api.worldweatheronline.com/free/v1/search.ashx"

class MarineWeather(WWOAPI):
    FREE_API_ENDPOINT = "http://api.worldweatheronline.com/free/v1/marine.ashx"
    PREMIUM_API_ENDPOINT = "http://api.worldweatheronline.com/premium/v1/marine.ashx"

class PastWeather(WWOAPI):
    FREE_API_ENDPOINT = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx"
    PREMIUM_API_ENDPOINT = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx"

    def __init__(self, q, date=None, **keywords):
        """ q and date are required for free API. sometimes date is optional for premium API """
        super(PastWeather, self).__init__(
            q, date=date, **keywords)

class TimeZone(WWOAPI):
    FREE_API_ENDPOINT = "http://api.worldweatheronline.com/free/v1/tz.ashx"
    PREMIUM_API_ENDPOINT = "http://api.worldweatheronline.com/free/v1/tz.ashx"

if __name__ == "__main__":
    """
    >>>
    10
    Patchy light rain
    http://www.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0017_cloudy_with_light_rain.png

    3
    Today: 2013-03-23, Max ℃: 3, Min ℃: -3, Light snow

    Date: 2013-03-23, Max ℃: 3, Min ℃: -3, Light snow
    Date: 2013-03-24, Max ℃: 0, Min ℃: -3, Light snow
    Date: 2013-03-25, Max ℃: 2, Min ℃: -3, Partly Cloudy

    weather = None [ObjectifiedElement]
        date = '2013-03-24' [StringElement]
        tempMaxC = 0 [IntElement]
        tempMaxF = 33 [IntElement]
        tempMinC = -3 [IntElement]
        tempMinF = 26 [IntElement]
        windspeedMiles = 18 [IntElement]
        windspeedKmph = 29 [IntElement]
        winddirection = 'ENE' [StringElement]
        winddir16Point = 'ENE' [StringElement]
        winddirDegree = 69 [IntElement]
        weatherCode = 326 [IntElement]
        weatherIconUrl = 'http://www.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0011_light_snow_showers.png' [StringElement]
        weatherDesc = 'Light snow' [StringElement]
        precipMM = 1.1 [FloatElement]

    The key is not valid.
    >>>
    """
    if internet_on() :
        #you need to change this to your own key.
        #you can get your own key from registering on WWO website
        if setKey("f077aef9b61e4110b3822001170509", "free"):
            weather = LocalWeather("shanghai")
            print weather.data.current_condition.temp_C
            print weather.data.current_condition.weatherDesc
            print weather.data.current_condition.weatherIconUrl

            print
            weather = LocalWeather("london", num_of_days=3)
            print len(weather.data.weather)
            today = weather.data.weather[0]
            tomorrow = weather.data.weather[1]
            twodayslater = weather.data.weather[2]
            print u"Today: %s, Max \u2103: %d, Min \u2103: %d, %s" %\
                (today.date, today.tempMaxC, today.tempMinC, today.weatherDesc)

            print
            for w in weather.data.weather:
                print u"Date: %s, Max \u2103: %d, Min \u2103: %d, %s" %\
                    (w.date, w.tempMaxC, w.tempMinC, w.weatherDesc)

            print
            print objectify.dump(tomorrow)

            print
        #you need to change this to your own key.
        #you can get your own key from registering on WWO website
        if setKey("f077aef9b61e4110b3822001170509", "premium"):
            weather = LocalWeather("new york")
            print
            print weather.data.current_condition.temp_C
            print weather.data.current_condition.weatherDesc
            print weather.data.current_condition.weatherIconUrl

            setKeyType("free")
            weather = LocalWeather("san francisco")
            print
            print weather.data.current_condition.temp_C
            print weather.data.current_condition.weatherDesc
            print weather.data.current_condition.weatherIconUrl
