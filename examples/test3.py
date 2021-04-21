try:
    import os
    import sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
except:
    pass

from flask import Flask, render_template, request
from flames import Flames
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/getflame', methods=['GET', 'POST'])
def getflame():
    if request.method == 'POST':
        nameA = request.form['nameA']
        nameB = request.form['nameB']

        if nameA.strip() != nameB.strip():
            f = Flames(nameA, nameB)

            r = f.find_it()
            return render_template('flame.html', status=r.title())
        else:
            return render_template('error.html', error="You can't FUCK yourself")


if __name__ == '__main__':
    app.run(debug=True, port=9090)
