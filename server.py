from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)
app.secret_key= "secret_key"

@app.route("/", methods=["GET"])
def vistaContador():
    if('contador' in session):
        session["contador"]+=1
    else:
        session["contador"]=1
    return render_template('index.html')

@app.route("/", methods=["POST"])
def aumentaContador():
    if 'contador' in session:
        print('el contador existe!')
        session["contador"]+=1
        return redirect("/count")
    else:
        print('el contador NO existe!')
        return redirect("/")

@app.route("/count", methods=["GET"])
def renderContadorCount():
    return render_template('index.html')

@app.route("/destroy_session", methods=["POST"])
def destroySession():
    session.clear()
    return redirect("/")

if (__name__=="__main__"):
    app.run(debug=True)