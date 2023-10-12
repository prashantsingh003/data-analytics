#!/bin/bash

url="https://www.amfiindia.com/spages/NAVAll.txt"
inputFile="input_data.txt"
outputFile="output.tsv"

# download file
curl -o "$inputFile" "$url"

# Extract data to outpuy file
awk -F';' '/^[0-9]/{print $4 "\t" $5}' "$inputFile" > "$outputFile"

echo "data extracted succesfully to ${outputFile}"
