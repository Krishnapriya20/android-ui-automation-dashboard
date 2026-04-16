import pandas as pd
import yaml
from adb_controller import ADBController
from actions import add_member

with open("config.yaml") as f:
    config = yaml.safe_load(f)

print("CONFIG LOADED:", config)

data = pd.read_csv("test_data.csv")

adb = ADBController(config['device']['id'])

results = []

for _, row in data.iterrows():
    try:
        add_member(adb, config, row)
        results.append({"user": row['first_name'], "status": "Success"})
    except Exception as e:
        print("ERROR:", e)
        results.append({"user": row['first_name'], "status": "Fail"})

pd.DataFrame(results).to_csv("report.csv", index=False)