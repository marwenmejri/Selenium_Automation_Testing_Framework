import json
import pandas as pd


def get_json_data(filename='../TestData/LoginData.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    output = []
    # print(data)
    for item in data:
        # print(item.values())
        # print(tuple(item.values()))
        output.append(tuple(item.values()))
    return output


def get_excel_data(filename='../TestData/LoginData.xlsx'):
    data = pd.read_excel(filename)
    output = []
    for index, row in data.iterrows():
        output.append(tuple(row))
    return output
