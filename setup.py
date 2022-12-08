# Xzavyer A. 2022

import os

print("\n\nNeed help? -> github.com/xzavyeradams/openai-discord")
print("Welcome to the setup process. This will generate a working config for the bot.")
apiKey = input("Please enter a API Key/Secret Key -> ")

while True:
    choice = input("Do you have multiple organizations? [Y/n] -> ")
    if choice == "Y" or choice == "y":
        organization = input("Please input the name of the organization you want to use for billing -> ")
        break
    elif choice == "N" or choice == "n":
        organization = ""
        print("Your DEFAULT organization will be billed when using this bot.")
        break
    else:
        print("Please respond with a valid option. [Y/n]")

while True:
    try:
        hardLimit = int(input("Please enter a maximum amount of tokens a user can use when making a request. -> "))
        break
    except TypeError:
        print("Please enter a number.")

