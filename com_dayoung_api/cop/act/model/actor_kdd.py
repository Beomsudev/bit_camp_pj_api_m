# import requests
# from bs4 import BeautifulSoup
# import re  # 정규식 사용
# from pandas import DataFrame


# class Crawling:
#     '''
#         Crawls data from wikipedia with following information
#         attributes: ['사진', '나이','이름','본명','종교','소속사', '배우자', '자녀','데뷔년도']
#         returns Dataframe with above attributes
#         '''
#     def __init__(self, actors_name=['이병헌'], gender='m'):
#         self.actors_name = [(actors_name, gender)]
#         self.gender = 'm'

#     def crawl(self):
#         # columns=['사진', '나이','이름','본명','종교','소속사', '배우자', '자녀','데뷔년도']
#         # url = "https://ko.wikipedia.org/wiki/"
#         # headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

#         actors_name = self.actors_name
#         actors_name = [("이병헌", "m"), ("전지현", "f"), ("손예진", "f"),
#                        ("안소희", "f"), ("강동원", "m"), ("하정우",  "m"),
#                        ("김혜수",  "f"), ("현빈",  "m"), ("송강호",  "m"),
#                        ("지창욱",  "m"), ("한효주",  "f"), ("정해인",  "m")]
#         # dont add these set
#         # redundant = set(["이병헌", "전지현", "손예진", "안소희", "강동원", "하정우",
#         #                  "김혜수", "현빈", "송강호", "지창욱",  "한효주",  "정해인"])

#         # actors_url = "https://namu.wiki/w/%EB%B0%B0%EC%9A%B0/%ED%95%9C%EA%B5%AD"
#         actors_name_2 = self.crawl_actors_name()
#         actors_name.extend(actors_name_2)
#         actor_id = 1
#         # actors_name = ["이병헌", "이진욱"]
#         actors_name = [('이병헌', "m")]
#         data = self.actors_to_df(actors_name, actor_id)
#         return data

#     def crawl_actors_name(self):
#         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
#         # url = self.url
#         url = "https://namu.wiki/w/%EB%B0%B0%EC%9A%B0/%ED%95%9C%EA%B5%AD"
#         res = requests.get(url, headers=headers)
#         res.raise_for_status()  # 혹시 문제가 있을시 에러)
#         soup = BeautifulSoup(res.text, 'lxml')
#         # 여기 까진 크롤링 하기 전 기본
#         # ---------------------------------------------------------------------
#         # 여기부터 크롤링 시작
#         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
#         res = requests.get(url, headers=headers)
#         res.raise_for_status()  # 혹시 문제가 있을시 에러
#         soup = BeautifulSoup(res.text, 'lxml')
#         list_div = soup.find_all('div', {'class': 'wiki-heading-content'})
#         elements = ""
#         actor = ""
#         actors_list = ""
#         actors2 = []
#         for elements in list_div:
#             actors_list = elements.find_all('li')
#             for actor in actors_list:
#                 if len(actor.text) == 3:
#                     actors2.append(actor.text)
#         return actors2

    