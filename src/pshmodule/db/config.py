from urllib.parse import quote

# import cryptocode

# db_key = os.environ.get("DB_KEY")
# data_source_dict = json.loads(cryptocode.decrypt(
#     "NR/+LcTXRqL7T3nRkS1tQYowur7i5es092yqs5zvU17d7+qEfI912lPaqXngfOuMQ84eZ9fH0ppNRQYPQ1myOqXOur/MolHc5YG3aoI7+7fu+78a5gKPUsMptbdlLCJd2SKm9qsiR7B69NXmt84rm2LIbdZBjuThPSNZ0qhR1tPqnwzlAjhkhp870b+IT7af/KY85UBmw1GMzYc7iFWrn7NRrFSM5BIzlUvuwzTTPwVeVH4TTBQFc6Tp6nYFVKmT7kbr/iq/QTgDxNoJdWPz4AHsNJXRbfBbqJAJPSjqYjm6zsTxdpf7Zqq9AXNYKQCOVhzjQiMWGCSi1VgLJmVLHzRZJUWJdms/8hz0/Jif5Zn1rTdlm7hqRkeeoZT4+cjoagOKON6WH3TBJ7H8c82Q7NFcAotAdpnd8g4fuecPz8ixL0yLfbGap5qN1eyBTLVcq5wKMTecx7oSVyzoNG5pwFgNRtUfCFHL5cvnyuQqvm2AZdVM04CrcFxewF+kfgYdM1kWFMYygGP3WsI1gZJpN6ES4aKNhrA/WU69xiAiN0k3/9AuIrBwxsL88iusOzYssUjWkv+tCnI7cg5IZz6qhYVtgru2w/wzaVBIb7gGuxg+C5VQ8oMbCD/8HOgQRwfjq+tXieN7zfnO3c1C4J7hbSqwKGXw9PP3kLN7Z+iCBgZjlvCijQJ0FYtx3HZSvn9PkivheWApTZUb39iixtkd/i8m/JyUzgWFdPVVB7ML9v93a+emKI2OmbQhz+4tsb556R76jmtp0lVoSgptOCo6ZGLAE0YNPSqdYUVK7knpE8h8yaKM8Mcl/uku3q3dNm4CytIUgvOOQeOrWBXJexb9ZxuH/hZD6p2Ax9pLpVaCPDDGsNy2Cz62mkcl/aWEKg6RJyohqhpbniD6U7Zc1dRiSVtX4jJIZ9ujoMMUGEh/a9N8ECACHN0pFuPFrmTJ1E/7FPwgPiU1Qm1SEXTZjKY3u7BXa0KJeOcUzo50I6H25K59HimhtSyTGsnpX/Cp+mcqEY1cmj0lkk4=*3fK03GBOrx4MFPPU9bxy5g==*ADyeSSdkRDfA6sLRHDvfAA==*bsKP/jXqXLSp4qh5rNSaaw==",
#     db_key,
# ))

def make_data_source(db_info, db_name):
    """
    Args:
        database_uri 생성 및 sqlalchemy engine 생성
        Args:
            db_info(str): 사용할 데이터베이스 서버 정보
            db_name(str): 사용할 데이터베이스 이름
    Returns:
        str: data_source
    """
    db_id = db_info["id"]
    password = db_info["pwd"]
    host = db_info["ip"]
    port = db_info["port"]
    
    data_source = (
        "mysql+pymysql://"
        + db_id
        + ":"
        + quote(password)
        + "@"
        + host
        + ":"
        + str(port)
        + "/"
        + db_name
    )
    return data_source
