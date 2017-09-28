#!/bin/bash

python ../composition/retrieveWeatherData.py London >london.txt
python ../scripts/generateStochasticSong.py London london.txt >london.xml
python ../scripts/upload.py london.xml london.wav

