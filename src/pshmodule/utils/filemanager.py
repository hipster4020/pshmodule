import os
import pickle

import openpyxl
import json
import pandas as pd


def load(path: str = ""):
    """
    확장자 별 file load
    Args:
        path (str): file path
    Returns:
        str: load data
    """
    check = os.path.isfile(path)
    try:
        data = []
        if check:
            extension = os.path.splitext(path)[1]
            print(f"extension : {extension}")

            # text
            if extension in (".txt", ".csv", ".tsv"):
                data = pd.read_csv(path, encoding="utf-8")
            # excel
            elif extension in (".xlsx", ".xls"):
                data = pd.read_excel(path)
            # pickle
            elif extension == ".pickle":
                with open(path, "rb") as f:
                    data = pickle.load(f)
            # json
            elif extension == ".json":
                """
                Read list of objects from a JSON lines file.
                """
                with open(path, 'r', encoding='utf-8') as f:
                    for line in f:
                        data.append(json.loads(line.rstrip('\n|\r')))
                data = pd.DataFrame(data)
            print("Loaded {} records from {}".format(len(data), path))
        else:
            raise print("The file does not exist.")
        return data
    except Exception as e:
        print(e)


def save(path: str, data):
    """
    확장자 별 file save
    Args:
        path (str): file path
        data : input data
    """
    check = os.path.isfile(path)
    try:
        if not check:
            extension = os.path.splitext(path)[1]

            # text
            if extension in (".txt"):
                with open(path, "w") as f:
                    for i in data:
                        f.write(str(i) + "\n")
            # excel
            elif extension in (".xlsx", ".xls"):
                data.to_excel(path)
            # pickle
            elif extension == ".pickle":
                with open(path, "wb") as f:
                    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
            # json
            elif extension == ".json":
                """
                Write list of objects to a JSON lines file for DeepLearning.
                """
                if 'label' in data.columns and 'content' in data.columns:
                    temp_dict = [{"content": row['content'].strip(), "label": row['label']} for _, row in data.iterrows()]
                    with open(path, 'w', encoding='utf-8') as f:
                        for line in temp_dict:
                            json_record = json.dumps(line, ensure_ascii=False)
                            f.write(json_record + '\n')
                else:
                    raise print("DataFrame' columns name no have 'content' or 'label'")
            print("Saved {} records".format(len(data)))
        else:
            raise print("file exists")
    except Exception as e:
        print(e)
