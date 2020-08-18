from flask_restful import Resource,reqparse
from flask import jsonify
session_reqparse = reqparse.RequestParser()   # 解析请求参数


session_reqparse.add_argument('name',type=str,location=['json'])  # 添加参数
session_reqparse.add_argument('password',type=str,location=['json'])

dic = {}
class SessionLogin(Resource):

    def get(self):
        print(dic,'--------------')
        return jsonify(dic)

    def post(self):
        args = session_reqparse.parse_args()
        print('This is args : {}'.format(args))
        name = args.name
        password = args.password
        if not name and not password:
            return jsonify({'code':100,'msg':'faile'})
        elif name and password:
            dic.update(args)
            print('login user is {} and his pwd is {}'.format(name,password))
            return jsonify({'code':200,'msg':'success'})

    def delete(self):
        args = session_reqparse.parse_args()
        name = args.name
        if name:
            del dic['name']
            return jsonify(dic)
        else:
            return jsonify({'code':200,'msg':'faile'})


    def put(self):
        pass

