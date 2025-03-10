from flask import Flask, render_template, url_for, request, redirect, render_template_string, flash, session, redirect, abort
from random import choice

app = Flask(__name__)
app.config["SECRET_KEY"] = "123jnfpgiujdfgi234123dfgdhytjkiol"
words = [
"Ты так красива, что я просто не могу отвести взгляд.", "Твои большие глаза смотрят мне прямо в сердце.", "Ты всегда выглядишь так свежо!",
    "Ты — воплощение изящества и очарования.", "ты для меня самая красивая и милая", "Ты так притягательна!", "Ты воплощение гармонии",
    "Между нами не только любовь, но и сила притяжения.", "Ты просто ослепительна!", "Быть рядом с тобой - лучшее время"]
nut = {18:"Эска", 15:"Пета", 12:"Пета", 9:"Гига", 6:"Мега", 3:"кило", 2:"Гекто", 1:"Дека", -1:"Деци", -2:"Санти", -3:"Милли", -6:"Микро", -9:"Нано", -12:"Пико", -15:"Фемто", -18:"Атто"}

def nearest(target, dictionary):
    near = float("inf")
    result = None
    lasts = None
    for num in dictionary:
        new_near = abs(target - num)
        if new_near < near:
            near = new_near
            result = num
            lasts = target - result
    return dictionary[result], lasts

@app.route("/", methods=["POST", "GET"])
def formula():


    if request.method == "POST":
        G = 6.67 * 10 ** -11
        F = G * float(request.form["mass_1"]) * float(request.form["mass_2"]) / (float(request.form["dist"]) ** 2)
        print(F)

        try:
            ind = str(F).index("e")
            after_e = str(F)[ind + 1:]
            number = str(F)[:ind]
            name, degree = nearest(int(after_e), nut)
            if degree == 0:
                New_F = f"{round(float(number), 4)} {name}"
            else:
                New_F =  f"{round(float(number), 4)} * 10^{degree} {name}"
        except ValueError:
            New_F = round(F, 4)

        return render_template("base.html", F=New_F, words=choice(words), nut=nut)
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if "userLogged" in session:
        return redirect(url_for("profile", login=session["userLogged"]))
    elif request.method == "POST" and request.form["login"] == "rind1" and request.form["password"] == "123":
        session["userLogged"] = request.form["login"]
        return redirect(url_for("profile", login=session["userLogged"]))
    return render_template("login.html")

@app.route("/profile/<login>")
def profile(login):
    if "userLogged" not in session or session["userLogged"] != login:
        abort(404)
    return render_template("account.html", name=login)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/tech", methods=["POST", "GET"])
def tech():
    if request.method == "POST":
        if len(request.form["name"]) > 2:
            flash("Спасибо за отзыв")
        else:
            flash("Ошибка отправки")
    return render_template("tech.html")

@app.errorhandler(404)
def no_page(error):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)