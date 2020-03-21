
import json
import os.path
import pandas as pd

file_path = os.path.join("./", "daily_summaries_FIPS10003_jan_2018_0.json")
with open(file_path) as f:
    data = json.load(f)

    df_0 = pd.DataFrame(data["results"])

print (df_0.shape)


file_path = os.path.join("./", "daily_summaries_FIPS10003_jan_2018_1.json")
with open(file_path) as f:
    data = json.load(f)
    df_1 = pd.DataFrame(data["results"])

print(df_1.shape)
