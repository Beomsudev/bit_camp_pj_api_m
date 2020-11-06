import os
import json
from flask import request
from flask_restful import Resource, reqparse
from com_dayoung_api.ext.db import db, openSession  # db 선택 Dayoungdb 에서
import pandas as pd
from com_dayoung_api.utils.file_helper import FileReader
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property


class UserDto(db.Model):  # 여기서 DB 모델 만든 것
    """
    [Creates User Model and corresponding table]
    """
    __tablename__ = 'users'  # 테이블 이름
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    # The __table_args__ attribute allows passing extra arguments to that Table

    # Creates table columns
    user_id: str = db.Column(db.String(30), primary_key=True, index=True)
    password: str = db.Column(db.String(30))
    fname: str = db.Column(db.String(30))
    lname: str = db.Column(db.String(30))
    age: int = db.Column(db.Integer)
    gender: str = db.Column(db.String(30))
    email: str = db.Column(db.String(80), unique=True)

    def __init__(self, user_id, password, fname, lname, age, gender, email):
        """
        Recives 7 parameters that are used to construct User Table
        user_id = 유저 고유 아이디 (Unique)
        password = 비밀번호
        fname = 성
        lname = 이름
        age = 나이
        gender = 성별
        email = 이메일 -> 나중에는 이메일이 아이디로 사용될 것 그래서 이것도 (Unique)
        """
        self.user_id = user_id
        self.password = password
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.email = email

    @hybrid_property
    def fullname(self):
        """
        성과 이름을 합쳐서 풀네임을 만들어서 return 한다
        returns fullname
        """
        if self.fname is not None:
            return self.fname + " " + self.lname
        else:
            return self.lname
    # some_user = session.query(User).first()
    # print(s()ome_user.fullname)
    # as well as usable within queries:
    # some_user = session.query(User).filter(User.fullname == "John Smith").first

    def json(self):
        """
        UserDto (User 모델)이 주어지면 json file 로 리턴한다 
        """
        return {
            'user_id': self.user_id,
            'password': self.password,
            'lname': self.lname,
            'age': self.age,
            'fname': self.fname,
            'gender': self.gender,
            'email': self.email
        }

    def __str__(self):
        """
        User id 를 리턴한다
        """
        return self.user_id


class UserVo:
    """
    User model 에 쓸 parameter 들을 생성 시킨다.
    """
    user_id: str = ''
    password: str = ''
    lname: str = ''
    fname: str = ''
    gender: str = ''
    age: int = 0
    email: str = ''