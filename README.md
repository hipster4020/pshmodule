# π€ AI Module

### ππ» λ°μ΄ν° μμ§, μ μ²λ¦¬, DB κ΄λ ¨ ν¨ν€μ§
#### pshmodule  https://pypi.org/project/pshmodule/
<br>
db :  sqlalchemy, pymysql excutemany query
<br>
processing : data μ κ·ννμ μ μ²λ¦¬
<br>
selenium : selenium ν¬λ‘€λ§
<br>
utils : filemanager νμΌ load, save λ° μ λ° utils
<br>

## ππ» use to
test directoryμ test νμΌλ‘ μμ μ°Έκ³  ex) alchemy_test, selenium_test
<br>
https://github.com/hipster4020/pshmodule/tree/master/test
<br>


## ππ» install
pip3 install pshmodule
<br>


## ππ» tree
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


## ππ» regist
python3 setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*