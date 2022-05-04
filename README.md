# 🤖 AI Module

### 👉🏻 데이터 수집, 전처리, DB 관련 패키지
<br>
db :  sqlalchemy, pymysql excutemany query
<br>
processing : data 정규표현식 전처리
<br>
selenium : selenium 크롤링
<br>
<br>

## 👉🏻 use to
test directory의 test 파일로 예시 참고 ex) alchemy_test, selenium_test
<br>
https://github.com/hipster4020/pshmodule/tree/master/test

<br>


## 👉🏻 tree
 * [src]
   * [pshmodule] 
     * [db]
       * [__init__.py]
       * [alchemy.py]
       * [config.py]
     * [processing]
       * [__init__.py]
       * [processing.py]
     * [selenium]
       * [__init__.py]
       * [helper.py]
     * [utils]
       * [__init__.py]
       * [filemanager.py]
     * [__init__.py]
 * [test]
   * [selenium_test.py] 
 * [README.md]
 * [setup.py]


## 👉🏻 regist
python3 setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*


## 👉🏻 install
pip3 install shpark-module
