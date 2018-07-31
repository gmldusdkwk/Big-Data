from flask import Flask, render_template, request

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from datetime import datetime
from flask_moment import Moment

from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '임희연'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECURITY_PASSWORD_SALT'] = '임희연'


moment = Moment(app)

db = SQLAlchemy(app)
admin = Admin(app, name='HeeYeon')

roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(), db.ForeignKey('user.id')), db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class SearchForm(FlaskForm):
    search = StringField('검색', validators=[DataRequired()])


class MyForm(FlaskForm):
    text = StringField('text', validators=[DataRequired()])


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

admin.add_view(ModelView(User, db.session))


def create_user():
    db.create_all()
    user_datastore.create_user(email='heeyeon@gmail.net', password='password')
    db.session.commit()


# Views
@app.route('/login')
@login_required
def home():
    return render_template('index.html')


@app.route('/')
def index():
    dt = datetime.utcnow()
    return render_template('index.html', dt=dt)


@app.route('/graph')
def graph():
    from data import plotdata
    script, div = plotdata()
    return render_template('graph.html', script=script, div=div)


@app.route('/0703', methods=['GET', 'POST'])
def hello_0703():
    dt = datetime(2018, 7, 3)
    return render_template('0703.html', dt=dt)


@app.route('/0705', methods=['GET', 'POST'])
def hello_0705():
    dt = datetime(2018, 7, 5)
    return render_template('0705.html', dt=dt)


@app.route('/0709', methods=['GET', 'POST'])
def hello_0709():
    dt = datetime(2018, 7, 9)
    return render_template('0709.html', dt=dt)


@app.route('/0717', methods=['GET', 'POST'])
def hello_0717():
    dt = datetime(2018, 7, 17)
    return render_template('0717.html', dt=dt)


@app.route('/0718', methods=['GET', 'POST'])
def hello_0718():
    dt = datetime(2018, 7, 18)
    return render_template('0718.html', dt=dt)


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = MyForm()
    if request.method == 'GET':  # GET 으로 하면 비밀번호가 다 보인다 그러므로 POST 로 해야한다.
        if form.validate_on_submit():
            return render_template('index.html')
        # print(a)
        # b = request.args['a']
        # print(b)
        # c = request.args.a
        # print(c)
        return render_template('search.html', form2=form)
    else:

        return render_template('search.html', form2=form)  # template 에서 사용하는 것 = 파이썬에서 쓰는 이름 (똑같이 쓰는 것을 추천)


@app.route('/form', methods=['GET', 'POST'])
def pandas_index():
    name = request.args.get('name')
    from pandas_ import pandas_index
    data = pandas_index()
    data2 = data[[name]]
    data2.to_html('/Users/limheeyeon/PycharmProjects/0727/templates/hhhh.html')
    return render_template('hhhh.html')


@app.route('/booking')
def booking():
    return render_template('booking.html')

if __name__ == '__main__':
    app.run()
