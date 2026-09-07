#!/bin/bash



# Purpose: Move all CSV and JSON files from the source folder into the json_and_CSV folder.

# Source directory containing the files 
SOURCE="."

# Destination directory 
DESTINATION="./json_and_CSV"

# Create the destination directory if it does not exist
mkdir -p "$DESTINATION"

echo "Starting file transfer..." 
echo "Source: $SOURCE" 
echo "Destination: $DESTINATION"
echo


#move all csv files
mv "$SOURCE"/*.csv "$DESTINATION/"
echo "CSV files moved successfully."


#move all or one json file
mv "$SOURCE"/*.json "$DESTINATION/"
echo "JSON files moved successfully."


echo 
echo "File transfer completed."

# Display the files now in the destination folder
echo "Files in $DESTINATION:"
ls -l "$DESTINATION"
