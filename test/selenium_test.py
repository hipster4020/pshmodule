import hashlib
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# pip3 install pshmodule test
from pshmodule.processing import processing as p
from pshmodule.selenium import Helper

# # 일반 test
#import src.pshmodule.selenium as test

# from src.pshmodule.processing import processing as p
# from src.pshmodule.selenium import Helper


def main():
    print("daum scrap start")
    category_url = "https://news.daum.net/breakingnews/200201"
    daum_helper.go_to(category_url)
    # title
    title = daum_helper.get_text_by_xpath(
        "/html/body/div[2]/div/div/div[1]/div[2]/ul/li[1]/div/strong/a",
    )
    # url
    url = daum_helper.get_attribute_by_xpath(
        "/html/body/div[2]/div/div/div[1]/div[2]/ul/li[1]/div/strong/a",
        "href",
    )
    # urlmd5
    urlmd5 = hashlib.md5(url.encode("utf-8")).hexdigest()
    # content
    daum_helper.go_to(url)
    body = daum_helper.get_text_by_xpath(
        "/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div[2]/div/section"
    )
    body = p.emoji_processing(body)
    body = p.news_preprocessing(body)

    # create_date
    dummy_date = daum_helper.get_text_by_xpath(
        "/html/body/div[2]/div[4]/div[1]/div/span/span[2]/span",
    )

    date = p.date_to_str(dummy_date, "daum")
    # image
    image_url = daum_helper.get_attribute_by_xpath(
        "/html/body/div[2]/div[4]/div[2]/div[1]/div[1]/div/div/section/figure/p/img",
        "src",
    )
    # media
    media = daum_helper.get_attribute_by_xpath(
        "/html/body/div[2]/div[4]/div[1]/div/em/a/img",
        "alt",
    )
    # daum_helper.back()  # page back

    print(f"title : {title}")
    print(f"url : {url}")
    print(f"urlmd5 : {urlmd5}")
    print(f"body : {body}")
    print(f"date : {date}")
    print(f"image_url : {image_url}")
    print(f"media : {media}")


if __name__ == "__main__":
    with Helper(
        "https://news.daum.net/breakingnews/",
        timeout=1,
    ) as daum_helper:
        # daum search
        main()
