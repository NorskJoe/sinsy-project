#!/usr/bin/python
import argparse

def skyScore(forecast):
    wordBank = \
    {
        'sunny':0.9,
        'clear':0.8,
        'haze':0.7,
        'overcast':0.6,
        'partly cloudy':0.5,
        'cloudy':0.4,
        'light drizzle':0.3,
        'light rain':0.3,
        'patchy rain':0.3,
        'moderate rain':0.2,
        'heavy rain':0.1,
        'thundery':0.1
    }

    if forecast.lower() in wordBank:
        return wordBank.get(forecast.lower())
    else:
        return 0.5


def tempScore(forecast):
    if forecast < 0:
        return 0.0
    elif forecast < 3:
        return 0.1
    elif forecast < 10:
        return 0.3
    elif forecast < 15:
        return 0.4
    elif forecast < 20:
        return 0.5
    elif forecast < 25:
        return 0.7
    elif forecast < 35:
        return 0.8
    else:
        return 0.2


def windScore(forecast):
    score = 0.0
    # Using Beaufort scale
    if forecast <  1:
        return 1.0
    elif forecast < 3:
        return 0.9
    elif forecast < 7:
        return 0.8
    elif forecast < 12:
        return 0.7
    elif forecast < 18:
        return 0.6
    elif forecast < 24:
        return 0.5
    elif forecast < 31:
        return 0.4
    elif forecast < 38:
        return 0.3
    elif forecast < 46:
        return 0.2
    elif forecast < 54:
        return 0.1
    else:
        return 0.0

    return score


def textScore(forecast):
    score = 0.0


    return score


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("weatherdata", default="-", type=argparse.FileType('r'), help="weather report for a city")
    args = parser.parse_args()

    data = args.weatherdata.read()
    lines = data.split('\n')

    skies = lines[0]
    temp = int(lines[1])
    wind = int(lines[2])
    text = lines[3]

    total = skyScore(skies)
    total += tempScore(temp)
    total += windScore(wind)
    total += textScore(text)

    print (total/4)
