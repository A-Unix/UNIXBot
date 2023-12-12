#!/usr/bin/python3

import openai
from dotenv import load_dotenv
import os
import subprocess
import time
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Load environment variables from .env file
load_dotenv()

# Check if colorama is installed
print("Cheking if coloram is already installed!")

# Install colorama using subprocess
subprocess.run(["pip", "install", "colorama"])

print("Please wait!")

time.sleep(2)

# Clear the terminal screen
os.system("clear")

import datetime
now = datetime.datetime.now()
print(Fore.BLUE + "Current date and time:")
print(Fore.CYAN + now.strftime("%d-%m-%Y %H:%M:%S"))

time.sleep(2)

import sys
print(Fore.GREEN + "Python version:")
print(Fore.RED + sys.version)
print(Fore.LIGHTMAGENTA_EX + "Python version:", sys.version_info)

time.sleep(2)

# Check if the script is running as root
print(Fore.BLUE + "Checking if the script is running as root!")

time.sleep(2)

#if os.geteuid() != 0:
 #   print(Fore.YELLOW + "This script is not running as root, please run it as root!")
  #  exit(1)

time.sleep(1)

# Get the API key from the environment variables
openai.api_key = os.getenv("API_KEY")

def chat_with_gpt3(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can experiment with different engines
        prompt=prompt,
        max_tokens=150  # Adjust based on your desired response length
    )

    return response.choices[0].text.strip()

def main():
    print(Fore.LIGHTMAGENTA_EX + "Welcome! You can chat with ChatGPT. Type 'exit' to end the conversation.")

    conversation_history = ""
    while True:
        user_input = input(Fore.LIGHTCYAN_EX + "You: ")
        if user_input.lower() == 'exit':
            break

        conversation_history += f"You: {user_input}\n"
        response = chat_with_gpt3(conversation_history)

        print(Fore.LIGHTBLUE_EX + f"ChatGPT: {response}")
        conversation_history += f"ChatGPT: {response}\n"

if __name__ == "__main__":
    main()
