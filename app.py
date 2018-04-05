from flask import Flask
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_bower import Bower
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bower(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/saracassella/database.db'
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)

admin = Admin(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

admin.add_view(MyView(name='Hello'))
admin.add_view(ModelView(Person, db.session))

if __name__ == '__main__':
    app.run(debug=True)
