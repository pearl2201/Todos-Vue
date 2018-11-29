from app import db
import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    done = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return '<%s>' % self.content
    
    @property
    def str_created(self):
        return self.created.strftime('%H:%M %d-%m-%Y')


