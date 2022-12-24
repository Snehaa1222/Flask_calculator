from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/",methods =["GET","POST"])
def home_page():
    return "Home Page"

@app.route("/math", methods=["POST"])
def calculator():
    if (request.method=="POST"):
        operation = request.json('operation')
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])

        if operation == 'add':
            r = num1+num2
            result = "The sum is: "+ str(r)
            return jsonify(result)

        if operation == 'sub':
            r = num1 - num2
            result = "The subtraction is: " + str(r)
            return jsonify(result)

        if operation == 'mul':
            r = num1 * num2
            result = "The multiplication is: " + str(r)
            return jsonify(result)

        if operation == 'divide':
            r = num1 / num2
            result = "The division is: " + str(r)
            return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)