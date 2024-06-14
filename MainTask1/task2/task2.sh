#!/bin/bash

app_url="http://127.0.0.1:5999/"

joke=$(curl -s $app_url | awk -F '"' '/joke/{print $4}')

count=$(echo "$joke" | wc -w)

echo "Number of words in the joke: $count"