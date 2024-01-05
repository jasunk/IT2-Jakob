import json, os

base = {
    "game": {
        "difficulty": 1  # faktor for skade gjort av fiende, mellom 0.1 og inf lowkey
    },
    "enemy": {
        "lvl": 1,
        "currentXP": 0,
        "XPtoLevelUp": 100,
        "sprite": 0
    },
    "player": {
        "lvl": 1,
        "currentXP": 0,
        "XPtoLevelUp": 100,
        "sprite": 0
    }
}

# Your initial data



def does_json_file_exist(file_path):
    return os.path.exists(file_path)


# Save data to a file
def updateSave():
    with open('save_data.json', 'w') as json_file:
        json.dump(save_1, json_file)

# Load data from the file
def loadSave():
    with open('save_data.json', 'r') as json_file:
        loaded_data = json.load(json_file)
        return loaded_data


if does_json_file_exist("save_data.json"):
    save_1=loadSave()
else:
    save_1 = base
updateSave()

# Now you can use loaded_data as your working data
print(loadSave()["player"])

def delete_json_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"The file '{file_path}' has been deleted.")
    else:
        print(f"The file '{file_path}' does not exist.")