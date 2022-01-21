from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)
app.secret_key= "secret_key"

@app.route("/", methods=["GET"])
def vistaContador():
    if('contador' in session):
        session["contador"]+=session["incremento"]
        session["contador_real"]+=1
    else:
        session["contador"]=1
        session["incremento"]=1
        session["contador_real"]=1
    return render_template('index.html')

@app.route("/", methods=["POST"])
def aumentaContador():
    if 'contador' in session:
        print('el contador existe!')
        if 'incremento' in session:
            session["incremento"]= int(request.form["incremento"])
            session["contador"]+=session["incremento"]
            session["contador_real"]+=1
        else:
            print("el valor de incremento no existe!")
            return redirect("/")
        return redirect("/count")
    else:
        print('el contador NO existe!')
        return redirect("/")

@app.route("/2", methods=["POST"])
def aumentaContador2():
    if 'contador' in session:
        print('el contador existe!')
        session["contador"]+=2
        session["contador_real"]+=1
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