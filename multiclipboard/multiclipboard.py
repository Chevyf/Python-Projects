from dataclasses import dataclass
import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

#function that create json file and save data to it
def save_json(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

#fuction that read the data and loads it
def load_json(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_json(SAVED_DATA)
# save command saves what ever is in the current clipbord to the json data file
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_json(SAVED_DATA, data)
        print("Saved!")
# load command loads key data to clipboard so you can paste
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Copy has been made to clipboard.")
        else:
            print("Key doesnt exist.")
#list prints out the Ket:value pairs listed on json document
    elif command == "list":
        print(data)

    else: 
        print("Invalid Command")
