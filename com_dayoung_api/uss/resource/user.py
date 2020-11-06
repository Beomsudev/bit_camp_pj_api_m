import os
import json
from flask import request
from flask_restful import Resource, reqparse
from com_dayoung_api.ext.db import db, openSession  # db 선택 Dayoungdb 에서
import pandas as pd
from com_dayoung_api.utils.file_helper import FileReader
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property

class Users(Resource):
    """
    서버와 정보를 주고 받는다.
    """
    @staticmethod
    def post():
        """
        모든 유저 정보를 데이터 베이스 안에 넣어준다
        """
        ud = UserDao()
        ud.bulk('users')

    @staticmethod
    def get():
        """
        데이터 베이스 안에 있는 모든 유저 정보를 찾아서 리턴해준다.
        """
        data = UserDao.find_all()
        print("list : ", type(data))
        return data, 200




class Delete(Resource):
    """
    정보를 받아와 유저 정보를 삭제 한다
    """
    @staticmethod
    def post(id: str):
        """
        Parameter: 유저 아이디를 받아온다.
        """
        UserDao.delete(id)