#!/bin/bash

#PERFORM ETL PROCESS USING THE GUIDE BELOW:
        #Extract: Download a CSV using the specified link. Save file into a folder called "raw". Have a confirmatory response to show it is saved correctly
        #Transform: Rename variables and select specified columns like year, units, etc
        #Save the content of the pre-selected columns into another file named 2023_year_finance_csv and housed in the folder called Transformed.
        #load transformed data into thee "Gold" directory (folder)

#EXTRACT

echo "Extracting Data"

#Source URL
readonly raw_data_url="https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisional.csv"

#Destination 
raw="./raw"

# Create raw folder if it doesn't exist
mkdir -p "$raw"

# Download the file
curl -L "$raw_data_url" -o "$raw/annual-enterprise-survey-2023.csv"

#Confirm the file is saved correctly
if [ -f "$raw/annual-enterprise-survey-2023.csv" ]
then
    echo "Folder exists. Proceeding with transforming..."
else
    echo "Raw data directory missing! Please create it first."
fi

#TRANSFORMATION

#Display top 5 rows with headers

echo "The top 5 rows are displayed for manual reading"
echo # a line break
head -n 5 raw/annual-enterprise-survey-2023.csv


