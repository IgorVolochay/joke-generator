import json

good_jokes = list()
for name in ['anekdote18.json', 'anekdote18(1).json', 'acho.json', 'poshlie_anekdote.json']:
    with open("dataset/raw_data/"+name, encoding='utf-8', mode="r") as json_file:
        json_data = json.load(json_file)
        json_file.close()

    for data in json_data["messages"]:
        if type(data["text"]) != list and data["text"] != "":
            good_jokes.append(data["text"])

for name in ["parsed.txt", "anek_utf8.txt"]:
    with open("dataset/raw_data/"+name, encoding='utf-8', mode="r") as text:
        raw_text = " ".join(text.readlines())
        spl_text = raw_text.split("<|startoftext|>")
        # print(spl_text[0:3])
        good_jokes.extend(spl_text[1:-1])

with open("dataset/dataset.json", encoding='utf-8', mode="r") as dataset_file:
    dataset = json.load(dataset_file)
    dataset_file.close()

good_jokes.extend(dataset["jokes"])
good_jokes = set(good_jokes)

dataset["jokes"] = list(good_jokes)

with open("dataset/dataset.json", encoding='utf-8', mode="w") as dataset_file:
    json.dump(dataset, dataset_file, indent=4, ensure_ascii=False)
    dataset_file.close()