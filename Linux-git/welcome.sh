#!/bin/bash
echo "Hello Data Engineers!"
echo "This is my first Bash script running on $(hostname)"

name="Lorreta"
role="data engineer"

echo "Hello, $name! Your role is $role."

current_date=$(date)
echo "The current date and time is: $current_date"

#reading user input

echo "Enter your project name:"
read project
echo "Creating project folder: $project"
mkdir -p "/projects/$project"

#Environment Variables: They are system defined already like $USER, $HOME, PWD, etc

echo "I am logged in as a $USER on $HOSTNAME"

#Exporting Variables: Used to make it available to child processes or other scripts

export DATA_PATH="/data/raw"

#FOR EXAMPLE

echo $DATA_PATH

#CONSTANTS and Read-only Variables
#to achieve this we use the "readonly command

readonly LOG_DIR="/var/logs/data"
#now, the path for LOG_DIR cannot be overwritten. It remains constant. This is Useful when i dont want anybody on the team to ever change a path.
LOG_DIR="tmp/logs" #This will cause an error


#CONDITIONAL STATEMENTS

if [ -f "data/raw/sales.csv" ]
then
	echo "File exists. Proceeding with processing..."
fi 
chmod +x welcome.sh





