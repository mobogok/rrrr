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
    import os
    
    port = int(os.environ.get("PORT", 5000))\
    app.run(host="0.0.0.0", port=port)
