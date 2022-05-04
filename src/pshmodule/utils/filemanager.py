import os
import pickle

import openpyxl
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
                data = pd.read_csv(path, sep="\n", header=None, encoding="")
            elif extension in (".xlsx", ".xls"):
                data = pd.read_excel(path)
            elif extension == ".pickle":
                with open(path, "rb") as f:
                    data = pickle.load(f)
            elif extension == ".json":
                data = pd.read_json(path)
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
                data.to_json(path, force_ascii=False)
            print("Saved {} records".format(len(data)))
        else:
            raise print("file exists")
    except Exception as e:
        print(e)
