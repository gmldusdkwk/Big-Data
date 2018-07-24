from flask import Flask, render_template

app = Flask(__name__)

# if user-agent가 mobile이라고 하면 render-template를 mobile 형식으로 return


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/x')
def hello_world1():
    # TODO 나 열심히 할게요
    return render_template('heeyeonblog.html')


@app.route('/c/<name>')
def hello_world2(name):
    # TODO 나 열심히 할게요
    return '<h1>%s</h1>'%name
    # 결과값을 받아서 제공한다.

@app.route('/a/<path>')
@app.route('/<path>')
def hello_world3(path=None):
    if path == path:
        return render_template('%s.html'%path)
    else:
        return render_template('heeyeonblog.html')


if __name__ == '__main__':
    app.run(debug=True)
