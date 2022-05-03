import pandas as pd
import pymysql
import sqlalchemy
from pshmodule.db.config import make_data_source


class DataSource:
    def __init__(self, db_info: dict, db_name: str):
        """
        database_uri 생성 및 sqlalchemy engine 생성
        Args:
            db_info(str): 사용할 데이터베이스 서버 정보
            db_name(str): 사용할 데이터베이스 이름
        """
        self.table_dict = {}
        # sqlalchemy
        self.database_uri = make_data_source(db_info, db_name)
        self.engine = sqlalchemy.create_engine(self.database_uri, pool_pre_ping=True)
        
        # pymysql
        self.conn = pymysql.connect(user=db_info["id"], passwd=db_info["pwd"], db=db_name, host=db_info["ip"], port=int(db_info["port"]), charset="utf8", use_unicode=True)

    def __enter__(self):
        return self.engine.begin()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.engine:
            self.engine.dispose()
        if self.conn:
            self.conn.close()
        print("-------------------------------" * 6)

    def __del__(self):
        if self.engine:
            self.engine.dispose()
        if self.conn:
            self.conn.close()
        print("-------------------------------" * 6)

    def df_to_sql(self, df: pd.DataFrame, table_name: str):
        """
        dataframe 형식으로 database insert 
        Args:
            df(DataFrame): 데이터베이스에 저장할 데이터프레임 객체
            table_name(str): 테이블 이름
        """
        print("execute start")
        df.to_sql(table_name, con=self.engine, if_exists="append", index=False)
        print("execute end")

    def execute_query(self, query: str):
        """
        simply query excute
        Args:
            query(str): 실행할 쿼리
        """
        try:
            print("execute start")
            with self.engine.begin() as con:
                result = con.execute(query)
                print("execute end")
                return result
        except Exception as e:
            print(e)
            
    def executemany_query(self, query: str, param: list):
        """
        pymysql excutemany 대량 query 실행
        Args:
            query(str): 실행할 쿼리
            param(list): 쿼리 set, where id 파라미터
            
            ex) query : "update table set column=%s where id=%s;"
                param : [('김', '1'), ('이', '2')]
        """
        try:
            print("executemany start")
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                result = cursor.executemany(query, param)
                self.conn.commit()
                print("executemany end")
                return result
        except Exception as e:
            print(e)

    def select_query_to_df(self, query: str):
        """
        select 쿼리 결과를 데이터프레임 형태로 반환
        Args:
            query(str): 실행할 쿼리
        """
        try:
            print("excute start")
            df = pd.read_sql(
                query,
                con = self.engine,
            )
            
            print(f"df's length : {len(df)}")
            print("excute end")
            
        except Exception as e:
            print(e)
        return df
