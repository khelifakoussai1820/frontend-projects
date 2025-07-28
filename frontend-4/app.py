from flask import Flask, render_template, request, redirect


import mysql.connector


app = app = Flask(
    __name__,
    template_folder="C:\\Users\\kouss\\coding\\Frontend-Projects\\frontend-4\\app\\templates",
)


database = mysql.connector.connect(
    host="localhost", user="root", password="Bluemoon 1894", database="AppleZone"
)

cursor = database.cursor()


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        email = request.form["email"]
        telephone = request.form["telephone"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "Les mots de passes ne correspondent pas"

        sql = "insert into Clients(nom, prenom,email,phone,password) values(%s,%s,%s,%s,%s)"
        val = (nom, prenom, email, telephone, password)

        cursor.execute(sql, val)

        database.commit()

        return "Ajouté avec succès"
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
