import os
import json
from flask import request
from flask_restful import Resource, reqparse
from com_dayoung_api.ext.db import db, openSession  # db 선택 Dayoungdb 에서
import pandas as pd
from com_dayoung_api.utils.file_helper import FileReader
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property


Session = openSession()
session = Session()
user_preprocess = UserPreprocess()


class UserDao(UserDto):
    """
        User 모델을 접근 하는 객체
        예: CRUD: (Create, Read, Update, Delete)
    """
    @staticmethod
    def bulk():
        """
        모든 유저 리스트를 DataBase 안에 넣어준다
        """
        df = user_preprocess.hook()
        print(df.head())
        session.bulk_insert_mappings(UserDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def count():
        """
        데이터 베이스 안에 몇명의 유저들이 있는지
        숫자를 리턴한다
        """
        return session.query(func.count(UserDto.user_id)).one()

    @staticmethod
    def update(user):
        """
        유저 정보를 수정해 준다
        새로운 유저 정보를 가진 유저를 가져와 기존의
        유저 정보를 수정해 준다.
        Parameter: 새로운 유저 정보를 가진 유저
        """
        Session = openSession()
        session = Session()
        print(f"{user.lname}")
        print(f"{user.fname}")
        session.query(UserDto).filter(UserDto.user_id == user.user_id).update({UserDto.lname: user.lname,
                                                                               UserDto.fname: user.fname,
                                                                               UserDto.age: user.age,
                                                                               UserDto.password: user.password,
                                                                               UserDto.age: user.age,
                                                                               UserDto.email: user.email})
        session.commit()
        session.close()

    @staticmethod
    def register(user):
        """
        새로운 유저를 parameter 로 가져온다.
        새로운 유저를 데이터베이스 안에 넣는다.
        """
        db.session.add(user)
        db.session.commit()

    @classmethod
    def delete(cls, id):
        """
        유저의 id 정보 (user_id) 를 가져와
        해당 id를 가진 유저를 데이터베이스에서
        삭제 시켜준다.
        """
        data = cls.query.get(id)
        db.session.delete(data)
        db.session.commit()
        session.close()


    @classmethod
    def find_all(cls):
        """
        데이터 베이스 안에 있는 모든 유저 정보를 찾는다
        Returns:
            제이슨 형식으로 데이터를 리턴해준다.
        """
        sql = cls.query
        df = pd.read_sql(sql.statement, sql.session.bind)
        return json.loads(df.to_json(orient='records'))

    @classmethod
    def find_by_name(cls, name):
        """
        주어진 이름을 토대로 유저를 찾아서
        해당 정보를 리턴해준다.
        """
        return session.query(UserDto).filter(UserDto.fname.like(f'%{name}%'))

    @classmethod
    def find_by_id(cls, user_id):
        """
        주어진 아이디를 토대로 유저를 찾아서
        해당 정보를 리턴해준다.
        """
        return session.query(UserDto).filter(UserDto.user_id.like(f'{user_id}')).one()

    @classmethod
    def login(cls, user):
        """
        유저 정보를 받아와, 해당 유저가 데이터베이스에 있는지 확인.
        확인 후, 있으면 로그인 시켜준다.
        Parameter: 유저 모델을 받아온다
        return: 유저 정보를 리턴해준다.
        """
        print("----------------login")
        sql = cls.query\
            .filter(cls.user_id.like(user.user_id))\
            .filter(cls.password.like(user.password))
        print("login type ", type(sql))
        df = pd.read_sql(sql.statement, sql.session.bind)
        print(json.loads(df.to_json(orient='records')))
        return json.loads(df.to_json(orient='records'))


if __name__ == "__main__":
    """
    데이터 베이스에 모든 유저 정보들을 넣어준다.
    """
    UserDao.bulk()


class User(Resource):
    """
    서버와 정보를 주고 받는다.
    """
    @staticmethod
    def put(id: str):
        """
        서버에서 해당 ID 의 새로운 유저 정보를 받아온다.
        정보를 토대로 해당 ID 유저의 정보를 바꿔서
        정보를 서버에 보내준다.
        parameter: 유저 아이디를 받아온다
        return: 새로운 유저 데이터를 리턴 한다
        """
        parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
        parser.add_argument('user_id', type=str, required=True,
                                                help='This field should be a user_id')
        parser.add_argument('password', type=str, required=True,
                                                help='This field should be a password')
        parser.add_argument('gender', type=str, required=True,
                                                help='This field should be a gender')
        parser.add_argument('lname', type=str, required=True,
                                                help='This field should be a lname')
        parser.add_argument('fname', type=str, required=True,
                                                help='This field should be a fname')
        parser.add_argument('email', type=str, required=True,
                                                help='This field should be a fname')
        parser.add_argument('age', type=int, required=True,
                                                help='This field should be a age')

        print("argument added")
        # def __init__(self, user_id, password,fname, lname, age, gender,email):
        args = parser.parse_args()
        print(f'User {args["user_id"]} updated')
        print(f'User {args["password"]} updated')
        user = UserDto(args.user_id, args.password, args.fname,
                       args.lname, args.age, args.gender, args.email)
        print("user created")
        UserDao.update(user)
        data = user.json()
        return data, 200

    @staticmethod
    def delete(id: str):
        """
        유저 아디를 받아와 해당 유저를 삭제한다.
        Parameter: 유저 아이디
        """
        UserDao.delete(id)
        print(f'User {id} Deleted')

    # @staticmethod
    # def post():
    #     """
    #     이거 아무것도 안하는데??
    #     """
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('user_id', type=str, required=True,
    #                                             help='This field should be a user_id')
    #     parser.add_argument('password', type=str, required=True,
    #                                             help='This field should be a password')
    #     args = parser.parse_args()
    #     print(f'User {args["id"]} added ')
    #     params = json.loads(request.get_data(), encoding='utf-8')
    #     if len(params) == 0:
    #         return 'No parameter'
    #     params_str = ''
    #     for key in params.keys():
    #         params_str += 'key: {}, value: {}<br>'.format(key, params[key])
    #     return {'code': 0, 'message': 'SUCCESS'}, 200

    @staticmethod
    def get(id: str):
        """
        유저 아이디를 받아와 해당 유저 객채를 리턴한다
        Parameter: User ID 를 받아온다
        return: 해당 아이디 유저 객채
        """
        print(f'::::::::::::: User {id} added ')
        try:
            user = UserDao.find_by_id(id)
            data = user.json()
            return data, 200
        except Exception as e:
            print(e)
            return {'message': 'User not found'}, 404

    # @staticmethod
    # def update():
    #     args = parser.parse_args()
    #     print(f'User {args["id"]} updated ')
    #     return {'code':0, 'message': 'SUCCESS'}, 200

    # @staticmethod
    # def delete():
    #     args = parser.parse_args()
    #     print(f'Us er {args["id"]} deleted')
    #     return {'code' : 0, 'message' : 'SUCCESS'}, 200