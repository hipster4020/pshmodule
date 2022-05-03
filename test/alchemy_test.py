import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# # pip3 install pshmodule test
# from pshmodule.db import alchemy

# 일반 test
from src.pshmodule.db import alchemy

import db_config


def main():
    # sql -> df
    result = alchemy.DataSource(db_config.db_info, "portal_news_scraper").select_query_to_df(
        "select title, content, keyword from indexing_news where id='154'"
    )
    print(result.head())

    # excutemany update
    # uquery = "update etc_news set content=%s where id=%s;"
    # param = [('null입니다.', '508268'), ('null입니다.', '508174')]
    
    # result = alchemy.DataSource(db_config.db_info, "news_scraper").executemany_query(
    #     uquery, param
    # )
    # print(result)



if __name__ == "__main__":
    main()
