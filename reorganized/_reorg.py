import json
import yaml
a = {}

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
i=0
while i<26:
    with open("C:\\Users\\surohv\\Documents\\GitHub\\dyinglanguages.github.io\\original-data\\"+letters[i]+".json", "r", encoding="UTF-8") as data:
        a.update(json.loads(data.read()))
    print(letters[i])
    i+=1
print(a["zoo"])

englishMarathiUntranslated = {}

for word in a:
    if "meanings" in a[word]:
        for meaning in a[word]["meanings"]:
            update = {
                meaning["id"]: {
                    "meaning": meaning["def"],
                    "word": word
                }
            }
            englishMarathiUntranslated.update(update)
            print(englishMarathiUntranslated[meaning["id"]]["word"])

wordBase = {}

for word in a:
    if "meanings" in a[word]:
        for meaning in a[word]["meanings"]:
            update = {
                meaning["id"]: {
                    "english-word": word,
                    "marathi-word": "",
                    "marathi-suggestion": "",
                    "marathi-confidence": 0
                }
            }
            wordBase.update(update)

with open("reorganized/englishMarathiUntranslated.json", "w") as f:
    json.dump(englishMarathiUntranslated, f)

with open("reorganized/wordBase.json", "w") as f:
    json.dump(wordBase, f)