import time
from manage import make_celery,app

my_celery = make_celery(app)

@my_celery.task
def check_name_pwd(name,pwd):
    for i in range(10):
        if name=='123' and pwd == '456':
            print('YES')
            time.sleep(1)

    return '1'
