import json

dictionary8 ={
    "copy_your_discord_id_there" : "user nickname",
    "or_as_many_other_ID_as_you_want" : "(optional)",
    "478866202371031040" : "disconnect"
}

dictionary ={
    "991335084986744932" : "тык Астрокреветки",
    "237301400676073484" : "баскетбольный клуб"
}

json_object = json.dumps(dictionary, indent=0)

"""
# Writing to sample.json
with open("channels_to_repost.json", "w") as outfile:
    outfile.write(json_object)
"""

# Opening JSON file
with open('id_users.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))

print()
for key, value in json_object.items():
    #print(f"{key}, {value}")
    pass

for key in json_object:
    print(f"{key}")

a = "478866202371031040"

if a in json_object.keys():
    print(True)
else:
    print(False)
