from flask import Flask, render_template, request
import os
app = Flask(__name__)

def exec(code, inp):
    with open("in", "wt") as f:
        f.write(inp)
    with open("code.wops", "wt") as f:
        print(code.replace('\r', ''))
        f.write(code)
    os.system("rm out; touch out; cat in | Wops/Wopslang code.wops >> out")
    with open("out", "r") as f:
        return f.readlines()

@app.route('/',methods=(['POST']))
def post():
    args = request.form
    res = ""
    cd = args['code'].replace('\r', '')
    inp = args['input'].replace('\r', '')
    for e in exec(cd, inp):
        res += e.replace("\n", "") + "\n"
    print(res)
    return render_template('index.html', inp=inp, code=cd, output=res)

@app.route('/')
def hello_world():
    return render_template('index.html', inp='Write your input here.', code='// Welcome to Wops Playground\n// You can edit and run your .wops code.\nout("Hello World!")', output='')

if __name__ == '__main__':
    app.run('0.0.0.0', port=9876, debug=True)
