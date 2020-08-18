from flask_restful import Resource,reqparse
from until.response_info import return_success_response
from enpoints.classes.operation import *
class_reqparse = reqparse.RequestParser()

class Classes(Resource):
    def get(self):
        args = class_reqparse.parse_args()
        name = args.name
        pwd = args.password
        print('name and pwd is {} {}'.format(name.pwd))
        # task = check_name_pwd.delay(name,pwd)
        task = check_name_pwd.apply_async(args=[name,pwd],countdown=60)
        print('This is task : {}'.format(task))
        return return_success_response(code=200,msg='success')

    def post(self):
        return return_success_response()

    def delete(self):
        return return_success_response()
