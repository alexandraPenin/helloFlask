from flask import Flask # import de l’objet Flask
import os
from flask import render_template
from flask import request

app = Flask(__name__) # instantiation application


PORT= os.environ.get("PORT") or 5000
HOST= os.environ.get("HOST") or "localhost"



@app.route("/") # association d’une route (URL) avec la fonction ‘home()’
def home():
    # if request.method=="GET":
    return render_template("index.html")
    # elif request.method=="POST":
    #     form_data=request.form
    #     return render_template("about.html", titre = "blabla")

@app.route("/about")
def about():
#       return "<p>Bienvenue chez moi</p>" # on renvoie une chaîne de caractères
    return render_template("about.html")

@app.route("/form", methods = ["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    elif request.method=="POST":
        form_data_f=request.form['fname']
        form_data_l=request.form['lname'],
        form_data_fav=request.form['fav_language']
        print(form_data_f)
        print(form_data_l)
        print(form_data_fav)
        with open("dataset.txt", "a") as f:
            f.write(f"{form_data_f},{form_data_l},{form_data_fav},\n")

        return render_template("form.html", titre = "Merci d'avoir complété ce formulaire")
#       return "<p>Bienvenue chez moi</p>" # on renvoie une chaîne de caractères
        # return render_template("form.html")



#open and read the file after the appending:

app.run(debug=True, host=HOST, port=PORT) # démarrage de l’application
# 127.0.0.1 -> localhost
# 0.0.0.0
