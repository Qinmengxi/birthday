from flask import *


app = Flask(__name__)

name = ''
login = ''
@app.route('/<int:id>', methods=['GET', 'POST'])
@app.route('/', methods=('GET', 'POST'))
def index(id=None):
    global name, login
    if request.method == 'POST':
        if request.form.get('account') == 'xiaosu' and request.form.get('pwd') == '19960322':
            login = 'success'
            name = 'admin'
            return render_template('1.html', name=name, login=login)
        else:
            login = 'fail'
        if id ==520:
            return render_template('index.html')
        if id ==1314:
            return render_template('3.html')
        if id ==666:
            return render_template('1.html')
    return render_template('hellow.html')

if __name__ == '__main__':
#    app.run(debug=True,host='0.0.0.0', port=8080)
    app.run(debug=True,host='0.0.0.0', port=5000)