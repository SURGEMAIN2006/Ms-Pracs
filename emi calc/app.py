from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    emi = None

    if request.method == "POST":
        principal = float(request.form["principal"])
        rate = float(request.form["rate"])
        time = int(request.form["time"])

        monthly_rate = rate / (12 * 100)
        months = time * 12

        emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

        emi = round(emi, 2)

    return render_template("index.html", emi=emi)

if __name__ == "__main__":
    app.run(debug=True)