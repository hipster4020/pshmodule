import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pshmodule",  # 프로젝트 이름
    version="0.1.5",  # 프로젝트 버전
    description="Modules related to preprocessing, crawling, collection, and preprocessing",  # 간단한 설명
    url="https://github.com/hipster4020/package-module",  # 프로젝트 주소
    author="shpark610",  # 작성자
    author_email="hipster4020@gmail.com",  # 작성자 이메일
    long_description=long_description,  # 프로젝트 설명, 보통 README.md로 관리
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[  # 설치시 설치할 라이브러리
        "sqlalchemy",
        "webdriver_manager",
        "selenium",
    ],
)
