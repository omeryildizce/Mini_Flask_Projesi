from flask import Flask, render_template, request, redirect, url_for
from rastgele_dizi import liste
app = Flask(__name__)

@app.route("/")
def index( ):
    return render_template("index.html")

@app.route("/toplam", methods=["GET", "POST"])
def toplam():
    if request.method == "POST":
        number1 = int(request.form.get("number1"))
        number2 = int(request.form.get("number2"))
        return render_template("number.html", total = number1 + number2)
    else:
        return redirect(url_for("index"))
        #return render_template("number.html")



    # numbers = liste(0,100, 50)
    # return render_template("index.html", numbers = numbers)
    #return render_template("index.html", number1 = 10, number2 = 20)
    # message1 =  "Bu bir mesajdır"
    # return render_template("index.html", message = message1)
# @app.route("/delete/item")
# def delete():
#     return "Delete Item"

# @app.route("/delete/<string:id>")
# def deleteId(id):
#     return f"Id: {id}"
if __name__ == "__main__":
    app.run(debug = True)



