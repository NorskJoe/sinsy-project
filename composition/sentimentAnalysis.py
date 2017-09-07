#!/usr/bin/python
import argparse
import re
import itertools
import sys
import nltk
from nltk.corpus import stopwords

wordBank = \
{
    'sunny':0.9,
    'clear':0.8,
    'haze':0.7,
    'overcast':0.6,
    'partly cloudy':0.5,
    'cloudy':0.4,
    'cloud':0.4,
    'light drizzle':0.3,
    'light rain':0.3,
    'rain':0.3,
    'patchy rain':0.3,
    'moderate rain':0.2,
    'heavy rain':0.1,
    'thundery':0.1
}

wordPairBank = \
{
    ('moderate','rain'):0.3,
    ('stay','dry'):0.7,
    ('dry','precipitation'):0.7,
    ('covering','0'):0.8,
    ('forecasted','sunny'):0.8,
    # ('',''):,
    # ('',''):,
    # ('',''):,
    # ('',''):,
    # ('',''):,
}

def skyScore(forecast):

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
    # Using Beaufort scale of  severity
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



def textScore(forecast):
    # Clean the forecast to remove all irrelevant words and punctuation
    cleanForecast = re.sub("[^a-zA-Z0-9]", " ", forecast).lower()

    # Create a list of all the meaningful words
    wordList = cleanForecast.split()
    meaningfulWordList = [w for w in wordList if not w in stopwords.words("english")]

    # Create list of tuples of each adjacent word
    # i.e "The weather is nice" will create:
    # (The, weather) (weather, is) (is, nice)
    a, b = itertools.tee(meaningfulWordList)
    next(b, None)
    wordPairList = zip(a, b)

    # Analyse word pairs against predefined word bank and obtain score
    total = 0.0
    for wordPair in wordPairList:
        if wordPair in wordPairBank:
            total += wordPairBank.get(wordPair)
    if total == 0.0:
        return 0.5
    else:
        return total/len(wordPairBank)



if __name__ == "__main__":

    lines = []
    for line in sys.stdin:
        lines.append(line)

    skies = lines[0]
    temp = int(lines[1])
    wind = int(lines[2])
    text = lines[3]

    total = skyScore(skies)
    total += tempScore(temp)
    total += windScore(wind)
    total += textScore(text)

    print (total/4)
