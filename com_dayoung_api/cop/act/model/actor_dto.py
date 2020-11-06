# from flask import request
# from flask_restful import Resource, reqparse
# import json
# from com_dayoung_api.ext.db import db, openSession
# import pandas as pd
# from sqlalchemy import func
# from com_dayoung_api.resources.crawling import Crawling


# class ActorPreprocess(object):
#     def __init__(self):
#         self.c = Crawling()  # 이병헌 is given as default

#         # print(self.dataFrame)

#     def hook(self):
#         dataFrame = self.c.crawl()
#         # print(dataFrame)
#         return dataFrame


# class ActorDto(db.Model):
#     __tablename__ = 'actors'
#     __table_args__ = {'mysql_collate': 'utf8_general_ci'}
#     # 'photoUrl', 'age', 'actor_id', 'name', 'realName', 'religion', 'agency',
#     #  'spouse', 'children', 'debutYear', 'gender', 'state'

#     # columns=['photoUrl', 'age','name','realName','religion','agency',
#     #          'spouse', 'children','debutYear','actor_id']
#     actor_id: str = db.Column(db.String(30), primary_key=True, index=True)
#     name: str = db.Column(db.String(30))
#     gender: str = db.Column(db.String(1))
#     age: str = db.Column(db.String(30))
#     real_name: str = db.Column(db.String(30))
#     religion: str = db.Column(db.String(30))
#     agency: str = db.Column(db.String(30))
#     spouse: str = db.Column(db.String(30))
#     children: str = db.Column(db.String(100))
#     debut_year: int = db.Column(db.Integer)
#     state: str = db.Column(db.String(1))
#     photo_url: str = db.Column(db.String(200))

#     def __init__(self, photo_url, actor_id, name, gender, age, real_name,
#                  spouse, children, debut_year, agency, religion, state):
#         self.photo_url = photo_url
#         self.actor_id = actor_id
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.real_name = real_name
#         self.religion = religion
#         self.agency = agency
#         self.spouse = spouse
#         self.children = children
#         self.debut_year = debut_year
#         self.state = state

#     def json(self):
#         return {
#             'photo_url': self.photo_url,
#             'actor_id': self.actor_id,
#             'name': self.name,
#             'gender': self.gender,
#             'age': self.age,
#             'real_name': self.real_name,
#             'spouse': self.spouse,
#             'children': self.children,
#             'debut_year': self.debut_year,
#             'religion': self.religion,
#             'agency': self.agency,
#             'state': self.state
#         }


# class ActorVo:
#     actor_id: str = ''
#     photo_url: str = ''
#     gender: str = ''
#     age: str = ''
#     name: str = ''
#     real_name: str = ''
#     religion: str = ''
#     agency: str = ''
#     spouse: str = ''
#     children: str = ''
#     debut_year: int = 0
#     state: str = '0'