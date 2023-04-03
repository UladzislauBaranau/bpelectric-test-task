import json

from datetime import datetime


with open('output.json', 'r+') as file:
    data = json.load(file)

    for d in data:
        d["updated"] = datetime.now().isoformat()

    file.seek(0)
    json.dump(data, file, indent=4)
