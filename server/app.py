#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    return string

@app.route('/print/<int:num>')
def count(num):
    result = '\n'.join(str(i) for i in range(num + 1))
    return result


@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    return f"The result of {num1} {operation} {num2} is {result}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
