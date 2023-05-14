"Unofficial Roblox Client Optimizer for macOS by LowSpecGamerROBLOX"

import logging
import os
import sys
import requests

from requests import Response

VERSION = "0.0.1"
ROBLOX_PATH = "/Applications/Roblox.app/Contents/MacOS/"
CLIENT_APP_SETTINGS_URL = "https://roblox-client-optimizer.simulhost.com/ClientAppSettings.json"


def print_logo() -> None:
    "Prints the installROC logo"

    print("\n")
    print("#################################################")
    print("# Roblox Client Optimizer Mac Installer         #")
    print("#  –––––––––––––––––––––––––––––––––––––––––––  #")
    print("# An unofficial ROC for macOS                   #")
    print("# VERSION: " + VERSION + "                                #")
    print("#################################################")
    print("\n")


def fetch_client_setting_json() -> Response:
    """
    Fetches the ClientAppSettings.json file from the official ROC website
    Returns the response
    """

    print("Fetching ClientAppSettings.json from the official website")

    return requests.get(CLIENT_APP_SETTINGS_URL, stream=True)


def main() -> None:
    "Main function"

    print_logo()

    if not os.path.exists(ROBLOX_PATH):
        logging.error("Roblox is not installed!")
        sys.exit(1)

    if not os.path.exists(ROBLOX_PATH + "ClientSettings"):
        print("ClientSettings does not exist, creating directory...")
        os.mkdir(ROBLOX_PATH + "ClientSettings")

    response = fetch_client_setting_json()

    if not response.ok:
        logging.error("Failed to fetch ClientAppSettings.json")
        sys.exit(1)

    with open(ROBLOX_PATH + "ClientSettings/ClientAppSettings.json", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

        print("Successfully fetched ClientAppSettings.json")

    print("Done! You can now launch Roblox with ROC enabled.")


if __name__ == "__main__":
    main()
else:
    logging.error("This file is not meant to be imported!")
    sys.exit(1)
