from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    
    if request.method == "POST":
        num1 = float(request.form.get("number_1"))
        num2 = float(request.form.get("number_2"))
        op = request.form.get("category")
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Cannot divide by zero"

    return render_template("web body.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)