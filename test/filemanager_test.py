import os
import sys

import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# pip3 install pshmodule test
from pshmodule.utils import filemanager as fm

## 일반 test
# from src.pshmodule.utils import filemanager as fm


def main():
    txt_path = "/home/shpark/team_ai/practice/data/sample.txt"
    excel_path = "/home/shpark/team_ai/practice/data/sample.xlsx"
    pickle_path = "/home/shpark/team_ai/practice/data/sample.pickle"
    json_path = "/home/shpark/team_ai/practice/data/sample.json"

    data = fm.load("/home/shpark/team_ai/practice/data/etc.txt")
    data = data.rename(columns={0: "value"})
    print(data)

    # save
    # text
    fm.save(txt_path, data.value.tolist())
    # excel
    fm.save(excel_path, data)
    # pickle
    fm.save(pickle_path, data)
    # json
    fm.save(json_path, data)

    # load
    # text
    df = fm.load(txt_path)
    print(df)
    print(type(df))
    # excel
    df = fm.load(excel_path)
    print(df)
    print(type(df))
    # pickle
    df = fm.load(pickle_path)
    print(df)
    print(type(df))
    # # json
    df = fm.load(json_path)
    print(df)
    print(type(df))


if __name__ == "__main__":
    main()
