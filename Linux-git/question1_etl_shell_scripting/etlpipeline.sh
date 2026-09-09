#!/bin/bash

#PERFORM ETL PROCESS USING THE GUIDE BELOW:
        #Extract: Download a CSV using the specified link. Save file into a folder called "raw". Have a confirmatory response to show it is saved correctly
        #Transform: Rename variables and select specified columns like year, units, etc
        #Save the content of the pre-selected columns into another file named 2023_year_finance_csv and housed in the folder called Transformed.
        #load transformed data into thee "Gold" directory (folder)

#EXTRACT

echo "Extracting Data"

#Source URL
export raw_data_url="https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisional.csv"
readonly raw_data_url

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
echo 
head -n 5 raw/annual-enterprise-survey-2023.csv

#create folder for transformed data
Transformed="./Transformed"
mkdir -p "Transformed"

#Renaming of column
INPUT_FILE="$raw/annual-enterprise-survey-2023.csv"
OUTPUT_FILE="$Transformed/2023_year_finance.csv"
OLD_COL="Variable_code"
NEW_COL="variable_code"

awk -v old="$OLD_COL" -v new="$NEW_COL" '
NR == 1 {

	#Rename the column specified
	gsub(old, new)
	

	#select required columns using the idea of for loop; to avoid hardcoding things
	for (i = 1; i<=NF; i++) {
		if ($i == "Year") Year = i
		if ($i == "Value") Value = i
		if ($i == "Units") Units = i
		if ($i == "variable_code") variable_code = i
	}
	
	#print the new header
	print "Year,Value,Units,variable_code"
	
	next
}
	#Select only the data from printed header
{
	print $Year "," $Value "," $Units "," $variable_code
}

' "$INPUT_FILE" > "$OUTPUT_FILE"

echo "Transformation is completed."
echo "Selected columns saved to: $OUTPUT_FILE"


#LOADING

#create the directory to dump the file
Gold="./Gold"
mkdir -p "Gold"

#copy the file 
cp "$Transformed/2023_year_finance.csv" "$Gold/"

#conditions to ensure file is copied
if [ -f "$Gold/2023_year_finance.csv" ]
then
	echo "loading completed successfully"
	echo "file saved to:  $Gold"
else
	echo "Loading failed. File was not saved to $Gold. Try again"
fi
