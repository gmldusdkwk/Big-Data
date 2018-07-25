from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '임희연'


class MyForm(FlaskForm):
    text = StringField('위치 선택 ', validators=[DataRequired()])


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/1', methods=['POST', 'GET'])
def visualization():
    form = MyForm()
    return render_template('1.html', form=form)


@app.route('/2')
def emoticon_List():
    return render_template('2.html')


@app.route('/3')
def clustering():
    return render_template('3.html')


if __name__ == '__main__':
    app.run()
