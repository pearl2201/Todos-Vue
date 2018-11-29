from flask import (Blueprint, flash, g, redirect,render_template,request,session,url_for,abort,jsonify)
import datetime
from flask_cors import CORS,cross_origin
bp = Blueprint('todos',__name__,url_prefix='/todos')
CORS(bp)
from app import db
from models import Todo

@bp.route('/',methods=['GET','POST'])
def all_todos():
    print ("todo")
    if request.method == 'POST':
        content = request.json['content']
        todo = Todo(content=content)
        db.session.add(todo)
        db.session.commit()
        return 'ok',200
    rows = Todo.query.all()
    todos = []
    for row in rows:
        todos.append({
            'id':row.id,
            'content':row.content,
            'created': row.str_created, 
            'done': row.done
        })
    return jsonify(todos)

@bp.route('/<int:id>/',methods=['GET','POST','DELETE','PUT'])
def  single_todo(id):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        Todo.query.filter_by(id=id).delete()
        db.session.commit()
        return 'ok',200
    elif request.method == 'PUT':
        todo = Todo.query.filter_by(id=id).first()
        todo.content=request.json["content"]
        todo.done = request.json["done"]
        print (todo)
        db.session.commit()
        return 'ok',200
    else:
        pass