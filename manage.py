from flask import Flask,g
from flask_restful import Api
from enpoints.login.resource import SessionLogin
from enpoints.classes.resource import Classes
from celery import Celery
from celery.result import AsyncResult
app = Flask(__name__)
api = Api(app)
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
def make_celery(app):
    # 异步队列
    celery = Celery(app.name, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery

# api.add_resource(SessionLogin,'/login/name',methods=['get'])
api.add_resource(SessionLogin,'/login')


api.add_resource(Classes,'/class')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
