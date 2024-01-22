import pandas as pd
import os
import json
from apath import theCSV, theJson

data = pd.read_csv(theCSV)
data_dict = data.to_dict(orient='records')
json_object = json.dumps(data_dict, indent=4)

with open(theJson, "w") as outfile:
    outfile.write(json_object)