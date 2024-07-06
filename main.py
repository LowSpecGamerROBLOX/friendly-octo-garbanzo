" Unofficial Roblox Client Optimizer for macOS by LowSpecGamerROBLOX "


import os
import sys
import requests
from colorama import Fore, init, Back
from requests import Response

init() # Colorama setup if something goes wrong :)

VERSION = "0.0.1"
ROBLOX_PATH = "/Applications/Roblox.app/Contents/MacOS/"
CLIENT_APP_SETTINGS_URL = "https://roblox-client-optimizer.simulhost.com/ClientAppSettings.json"

def log(context) -> None:
    """
    Logs to console with info theme
    """
    print(Fore.BLACK + Back.WHITE + "INFO  |" + str(context))

def err(context) -> None:
    """
    Logs to console with error theme
    """
    print(Fore.BLACK + Back.RED +   "ERROR | " + str(context))

def print_logo() -> None:
    "Prints the installROC logo"

    print("\n")
    print("#################################################")
    print("#" + Fore.RED + " Roblox " + Fore.RESET + "Client " + Fore.RED + "Optimizer " + Fore.RESET + "Mac " + Fore.RED + "Installer" + Fore.RESET + "         #")
    print("#                                               #")
    print("# An unofficial ROC for macOS                   #")
    print("# VERSION: " + Fore.RED + VERSION + Fore.RESET + "                                #")
    print("#################################################")
    print("\n")


def fetch_client_setting_json() -> Response:
    """
    Fetches the ClientAppSettings.json file from the official ROC website
    Returns the response
    """

    log("Fetching ClientAppSettings.json from the official website")

    return requests.get(CLIENT_APP_SETTINGS_URL, stream=True)


def main() -> None:
    "Main function"

    print_logo()

    if not os.path.exists(ROBLOX_PATH):
        err("Roblox is not installed or found on path!")
        sys.exit(1)

    if not os.path.exists(ROBLOX_PATH + "ClientSettings"):
        log("ClientSettings does not exist, creating directory...")
        os.mkdir(ROBLOX_PATH + "ClientSettings")

    response = fetch_client_setting_json()

    if not response.ok:
        err("Failed to fetch ClientAppSettings.json")
        sys.exit(1)

    with open(ROBLOX_PATH + "ClientSettings/ClientAppSettings.json", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

        log("Successfully fetched ClientAppSettings.json")

    log("Done! You can now launch Roblox with ROC enabled.")


if __name__ == "__main__":
    main()
else:
    err("This file is not meant to be imported!")
    sys.exit(1)
