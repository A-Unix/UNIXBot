#!/bin/bash

echo -e "\nUpdating your system, please wait\n"
sleep 1

# Update system
apt update

# Install pip
apt install python3-pip -y

echo -e "\nInstalling required dependencies, please wait!\n"
sleep 1

git rm --cached .env
git commit -m "Untrack .env file"

# Install required dependencies
pip install openai
pip install --upgrade openai
openai migrate
pip install python-dotenv

echo -e "\nDone, run the 'main.py' file now!\n"
sleep 1