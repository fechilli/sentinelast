from flask import Flask, render_template



app = Flask(__name__)

#criar a primeira pagina do site
@app.route("/") #rotas
def homepage(): #função que define o que será mostrado
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("home.html")



#colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)

##servidor do heroku
