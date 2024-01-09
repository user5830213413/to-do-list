from flask_restful import Resource, reqparse

from app.models import Task, db

task_parser = reqparse.RequestParser()
task_parser.add_argument('title', type=str, required=True)
task_parser.add_argument('description', type=str)

put_parser = reqparse.RequestParser()
put_parser.add_argument('title', type=str)
put_parser.add_argument('description', type=str)

class TaskListResource(Resource):
    def get(self):
        return [{'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done} for task in Task.get_all_task()]
    
    def post(self):
        data = task_parser.parse_args(strict=True)

        task = Task(title=data['title'], description=data['description'])
        db.session.add(task)
        db.session.commit()

        return {'message': 'задача успешно создана!', 'id': task.id}, 201
    


class TaskResource(Resource):
    def get(self, task_id):
        task = Task.get_task_by_id(task_id)
        if not task:
            return {'message': 'задача не найдена'}, 404
        return task.json(), 200
    
    def put(self, task_id):
        task = Task.get_task_by_id(task_id)
        if not task:
            return {'message': 'задача не найдена для изменения'}, 404
        
        task_parser_copy = task_parser.copy()
        task_parser_copy.add_argument('done', type=bool, required=True)

        data = task_parser_copy.parse_args(strict=True)

        task.title = data['title']
        task.description = data['description']
        task.done = data['done']

        task.save_db()

        return {'message': 'задача успешно обновлена'}, 200

    def delete(self, task_id):
        task = Task.get_task_by_id(task_id)
        if not task:
            return {'message': 'задача не найдена для удаления'}, 404
        task.delete_db()
        return {'message': 'задача успешно удалена!'}, 200