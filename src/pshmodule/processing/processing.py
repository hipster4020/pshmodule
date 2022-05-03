import datetime
import re


class Processing:
    # def __init__(self, content: str):
    #     self.content = content

    def date_to_str(self, str_date: str, portal: str) -> str:
        """
        날짜 형식 DataBase Format 처리 작업
        Args:
            str_date (str): date formated string text by portal site
        Returns:
            str: processed text
        """
        if portal == "daum":
            if str_date == "" or str_date == " " or str_date is None:
                str_date = str(datetime.datetime.now())
                str_date = str_date[:19]
                str_date = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
            else:
                # str_date = str_date.replace(" ", "")
                str_date = datetime.datetime.strptime(str_date, "%Y. %m. %d. %H:%M").strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
        elif portal == "naver":
            if str_date == "" or str_date == " " or str_date is None:
                str_date = str(datetime.datetime.now())
                str_date = str_date[:19]
                str_date = datetime.datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")

            elif str_date.endswith("일전"):
                datenum = str_date.replace("일전", "").replace(" ", "")
                str_date = str(datetime.datetime.now() - datetime.timedelta(days=int(datenum)))
                str_date = str(str_date[:11]) + "00:00:00"

            elif str_date.endswith("시간전"):
                datenum = str_date.replace("시간전", "").replace(" ", "")
                str_date = str(datetime.datetime.now() - datetime.timedelta(hours=int(datenum)))
                str_date = str(str_date[:19])

            elif str_date.endswith("분전"):
                datenum = str_date.replace("분전", "").replace(" ", "")
                str_date = str(
                    datetime.datetime.now() - datetime.timedelta(minutes=int(datenum))
                )
                str_date = str(str_date[:19])

            else:
                if str_date.startswith("기사입력"):
                    str_date = str_date.replace("기사입력 ", "")
                str_date = (
                    str_date.replace("오전", "AM")
                    .replace("오후", "PM")
                    .replace("오 전", "AM")
                    .replace("오 후", "PM")
                )
                str_date = datetime.datetime.strptime(str_date, "%Y.%m.%d. %p %I:%M").strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
        return str(str_date)

    def emoji_processing(self, content: str) -> str:
        """
        이모지 처리
        Args:
            content (str): string content

        Returns:
            str: processed content
        """
        
        emoji_pattern = re.compile(
            "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "]+",
            flags=re.UNICODE,
        )
        content = emoji_pattern.sub(r"", str(content))  # no emoji

        return content

    def news_preprocessing(self, content: str) -> str:
        """
        특수문자 및 본문 외 불필요 텍스트 제거 작업
        Args:
            content (str): string content

        Returns:
            str: processed content
        """
        
        result = (
            str(content).replace("뉴스코리아", "")
            .replace("및", "")
            .replace("Copyright", "")
            .replace("copyright", "")
            .replace("COPYRIGHT", "")
            .replace("저작권자", "")
            .replace("ZDNET A RED VENTURES COMPANY", "")
            .replace("appeared first on 벤처스퀘어", "")
            .replace("appeared first on 벤처 스퀘어", "")
            .replace("appeared first on 모비인사이드 MOBIINSIDE", "")
            .replace("appeared first on 모비 인사이드 MOBIINSIDE", "")
            .replace("The post", "")
        )
        result = re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", result)
        result = re.sub(r"[a-zA-Z가-힣]+뉴스", "", result)
        result = re.sub(r"[a-zA-Z가-힣]+ 뉴스", "", result)
        result = re.sub(r"[a-zA-Z가-힣]+newskr", "", result)
        result = re.sub(r"[a-zA-Z가-힣]+Copyrights", "", result)
        result = re.sub(r"[a-zA-Z가-힣]+ Copyrights", "", result)
        result = re.sub(r"\s+Copyrights", "", result)
        result = re.sub(r"[a-zA-Z가-힣]+com", "", result)
        result = re.sub(r"[가-힣]+ 기자", "", result)
        result = re.sub(r"[가-힣]+기자", "", result)
        result = re.sub(r"[가-힣]+ 신문", "", result)
        result = re.sub(r"[가-힣]+신문", "", result)
        result = re.sub(r"데일리+[가-힣]", "", result)
        result = re.sub(r"[가-힣]+투데이", "", result)
        result = re.sub(r"[가-힣]+미디어", "", result)
        result = re.sub(r"[가-힣]+ 데일리", "", result)
        result = re.sub(r"[가-힣]+데일리", "", result)
        result = re.sub(r"[가-힣]+ 콘텐츠 무단", "", result)
        result = re.sub(r"전재\s+변형", "전재", result)
        result = re.sub(r"[가-힣]+ 전재", "", result)
        result = re.sub(r"[가-힣]+전재", "", result)
        result = re.sub(r"[가-힣]+배포금지", "", result)
        result = re.sub(r"[가-힣]+배포 금지", "", result)
        result = re.sub(r"\s+배포금지", "", result)
        result = re.sub(r"\s+배포 금지", "", result)
        result = re.sub(r"[a-zA-Z가-힣]+.kr", "", result)
        result = re.sub(r"/^[a-z0-9_+.-]+@([a-z0-9-]+\.)+[a-z0-9]{2,4}$/", "", result)
        result = re.sub(r"[\r|\n]", "", result)
        result = re.sub(r"\[[^)]*\]", "", result)
        result = re.sub(r"\([^)]*\)", "", result)
        result = re.sub(r"[^ ㄱ-ㅣ가-힣A-Za-z0-9]", "", result)
        result = re.sub(r"이 글은 외부 필자인 +[a-zA-Z가-힣]", "", result)
        result = re.sub(r"[a-zA-Z가-힣]+기고입니다.", "", result)
        result = result.replace(".", " ")
        result = result[:result.find('관련기사')]
        result = result[:result.find('관련 기사')]
        result = result.strip()

        return result        
