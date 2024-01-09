from flask import Flask
from flask_restful import Api

from config import Config
from app.models import db, Task

app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()



from app.resources import TaskListResource, TaskResource

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/task/<int:task_id>')