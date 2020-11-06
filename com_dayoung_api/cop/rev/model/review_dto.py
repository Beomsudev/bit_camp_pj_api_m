# from typing import List
# from flask_restful import Resource, reqparse
# from flask import request
# import json
# from flask import jsonify
# import pandas as pd
# import numpy as np
# import os
# from com_dayoung_api.utils.file_helper import FileReader
# from com_dayoung_api.resources.movie import RecoMovieDto, RecoMovieDao
# from pathlib import Path
# from com_dayoung_api.ext.db import db, openSession
# from sqlalchemy.orm import Session, sessionmaker
# from sqlalchemy import create_engine
# from sqlalchemy import func
# # from com_dayoung_api.user.dto import UserDto
# # from com_dayoung_api.movie.dto import MovieDto

# # config = {
# #     'user' : 'root',
# #     'password' : 'root',
# #     'host': '127.0.0.1',
# #     'port' : '3306',
# #     'database' : 'dayoungdb'
# # }
# # charset = {'utf8':'utf8'}
# # url = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8"
# # engine = create_engine(url)

# class ReviewDto(db.Model):
#     __tablename__ = "reviews"
#     __table_args__ = {'mysql_collate':'utf8_general_ci'}
    
#     rev_id: int = db.Column(db.Integer, primary_key=True, index=True)
#     title: str = db.Column(db.String(100))
#     content: str = db.Column(db.String(500))
#     label: int = db.Column(db.Integer)
     
#     user_id: str = db.Column(db.String(30)) # db.ForeignKey(UserDto.user_id
#     movie_id: int = db.Column(db.Integer, db.ForeignKey(RecoMovieDto.movieid))
    
#     # movie = db.relationship('MovieDto', back_populates="reviews")
    
#     def __init__(self, title, content, label, user_id, movie_id):
#         self.title = title
#         self.content = content
#         self.label = label
#         self.user_id = user_id
#         self.movie_id = movie_id
        
#     def __repr__(self):
#         return f'rev_id = {self.rev_id}, user_id = {self.user_id}, movie_id = {self.movie_id},\
#             title = {self.title}, content = {self.content}, label = {self.label}'
    
#     def json(self):
#         return {
#             'rev_id' : self.rev_id,
#             'user_id' : self.user_id,
#             'movie_id' : self.movie_id,
#             'title' : self.title,
#             'content' : self.content,
#             'label' : self.label
#         }
        
# class ReviewVo:
#     rev_id: int = 0
#     title: str = ''
#     content: str = ''
#     label: int = 0
#     user_id: str = ''
#     movie_id: int = 0