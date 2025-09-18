from flask import Flask, render_template, request, redirect
import database_manager as dbHandler

app = Flask(__name__)


# Root redirects to sign-in
@app.route('/')
def root():
    return redirect("/signin")


# Sign-in page
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simple login check
        if username and password:
            return redirect("/homepage")
        else:
            error = "Please enter both username and password."
            return render_template("signin.html", error=error)

    return render_template("signin.html")


# Homepage
@app.route('/homepage')
def homepage():
    data = dbHandler.listExtension()  # optional
    return render_template('partials/homepage.html', content=data)


@app.route("/friends")
def friends():
    return render_template("friends/friends.html")


@app.route("/settings")
def settings():
    return render_template("settings/settings.html")


@app.route("/maths")
def maths_chat():
    return render_template("groups/maths_chat.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)
