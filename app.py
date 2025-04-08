from flask import Flask, render_template, request

app = Flask(__name__)

feedback_data = []

@app.route("/")
def index():
    return render_template("contact_form.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        subject = request.form["subject"]
        feedback_data.append({"name": name, "email": email, "phone": phone, "message": message, "subject": subject})


if __name__ == "__main__":
    app.run(debug=True)