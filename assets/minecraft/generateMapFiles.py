import os, json

files = os.listdir("textures/map/")

i = 999

# finalfile = '{"parent": "item/generated","textures": {"layer0": "item/map","layer1": "item/map_overlay"},"overrides": ['

for fullfilename in files:
    i += 1
    filename = fullfilename.split(".")[0]
    
    # print('MapLookup.put("' + filename + '", ' + str(i) + ');')

    js = '{"parent": "minecraft:item/generated", "textures": {"layer0": "minecraft:map/abcdabcd"}, "display": {"gui": {"scale": [1.2, 1.2, 1.2]}}}'
    js = js.replace("abcdabcd", filename)

    # file = open(f"models/custom/map/{filename}.json", "r")

    # current_file = json.loads(file.read())

    # current_file["display"] = {
    #     "gui": {
    #         "scale": [1.2, 1.2, 1.2]
    #     }
    # }

    file = open(f"models/custom/map/{filename}.json", "w")


    file.write(js)

    # file.write(json.dumps(json.loads('{"parent": "minecraft:item/generated","textures": {"layer0": "minecraft:map/' + filename + '"}}')))
    
    # predicate = '{"predicate": {"custom_model_data": ' + str(i) + '},"model": "custom/map/' + filename + '"},'

    # finalfile += predicate


# finalfile += ']}'
# mapfile = open("models/item/map.json", "w").write(finalfile);