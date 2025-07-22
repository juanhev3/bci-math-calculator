from flask import Flask, render_template, request, jsonify
import re  # For input validation

app = Flask(__name__)
current_result = "0"

def sanitize_math_input(expr):
    """Allow only basic math expressions with numbers and +-*/()"""
    if not re.match(r'^[\d\+\-\*\/\(\)\s]+$', expr):  # Only these chars allowed
        return None
    try:
        # Safe evaluation with limited operators
        return str(eval(expr, {"__builtins__": None}, {}))  # <- Parenthesis fixed
    except:
        return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    global current_result
    expression = request.form.get("expression", "")
    
    # Special cases for gestures
    if expression == "1+1":
        current_result = "2"
    elif expression == "0":
        current_result = "0"
    else:
        # General math validation
        result = sanitize_math_input(expression)
        if result:
            current_result = result
        else:
            current_result = "Invalid input"
    
    return jsonify({"result": current_result})

@app.route("/get_result")
def get_result():
    return jsonify({"result": current_result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)