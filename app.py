from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_cors import CORS

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'


# enable CORS


db = SQLAlchemy(app)
migrate = Migrate(app, db)



import todo
app.register_blueprint(todo.bp)
app.add_url_rule('/',endpoint='index')
CORS(app)

app.route('/')
app.route('/index/')
def index():
    return 'ping',200

@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()



if __name__ =="__main__":

    app.run(debug=True)