# Xzavyer A // Xzavyer.dev

import os
import json

print("\n\nNeed help? -> github.com/xzavyeradams/openai-discord")
print("Welcome to the setup process. This will generate a working config for the bot.")

try:
    open("config.json", "r")
    input("It seems you already have a config saved, you can edit this config by opening it with your preferred text editor.")
except FileNotFoundError:
    apiKey = input("Please enter a API Key/Secret Key -> ")

    while True:
        choice = input("Do you have multiple organizations? [Y/n] -> ")
        if choice == "Y" or choice == "y":
            organization = input("Please input the name of the organization you want to use for billing -> ")
            break
        elif choice == "N" or choice == "n":
            organization = "default"
            print("Your DEFAULT organization will be billed when using this bot.")
            break
        else:
            print("Please respond with a valid option. [Y/n]")

    while True:
        try:
            hardLimit = int(input("Please enter a maximum amount of tokens a user can use when making a single request. -> "))
            break
        except TypeError:
            print("Please enter a number.")

    token = input("Please enter a Discord bot token for the bot to be hosted on -> ")

    print("\nHere is a preview of your config:")
    print("OpenAI API/Secret Key: " + apiKey)
    print("OpenAI Organization": + organization)
    print("Max Tokens: " + hardLimit + " tkns/req")
    print("Discord tkn: " + token)
    print("\nYou can always change this later inside config.json.")

    json.dump(open("config.json", "w"))