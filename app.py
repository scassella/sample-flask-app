from flask import Flask, redirect, render_template, session
from flask.views import MethodView
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_bower import Bower
from flask_sqlalchemy import SQLAlchemy
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from onelogin.saml2.utils import OneLogin_Saml2_Utils

app = Flask(__name__)
Bower(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/saracassella/database.db'
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)

admin = Admin(app, base_template='admin/master_base.html')


def isUserAuthenticated():
    print(session)


class FrontpageView(MethodView):
    def get(self):
        return redirect('/admin')


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))


class Index(BaseView):
    @expose('/')
    def index(self):
        person = Person
        isUserAuthenticated()
        return self.render('index.html', Person=person)


class Dashboard(BaseView):
    @expose('/')
    def index(self):
        return self.render('dashboard.html')


class Models(BaseView):
    @expose('/')
    def index(self):
        return self.render('models.html')


class Users(BaseView):
    @expose('/')
    def index(self):
        return self.render('users.html')


admin.add_view(Dashboard(name='Dashboard'))
admin.add_view(Models(name='Models'))
admin.add_view(Users(name='Users'))
admin.add_view(ModelView(Person, db.session))
app.add_url_rule(
    '/',
    view_func=FrontpageView.as_view('FrontpageView'),
    methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
