from app.models.db import db

class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done
        }
    
    @classmethod
    def get_task_by_id(cls, task_id):
        """
        возвращает задачу по id
        """
        return cls.query.filter_by(id=task_id).first()
    
    @classmethod
    def get_all_task(cls):
        """
        возвращает все задачи
        """
        return cls.query.all()
    
    def save_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_db(self):
        db.session.delete(self)
        db.session.commit()