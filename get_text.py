import json

normal_joke_counter = 0
ad_joke_counter = 0
for name in ['anekdote18.json', 'anekdote18(1).json', 'acho.json', 'poshlie_anekdote.json']:
    with open("raw_datasets/"+name, encoding='utf-8', mode="r") as file:
        json_data = json.load(file)
        file.close()

    for data in json_data["messages"]:
        if type(data["text"]) != list:
            #print(data["text"], end="\n  ---  \n")
            normal_joke_counter += 1
        else:
            ad_joke_counter += 1

print(normal_joke_counter, ad_joke_counter)