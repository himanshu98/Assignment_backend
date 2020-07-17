from flask import request
import json
from app import app

from sympy import symbols, Function, simplify, factor, solve
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)


@app.route('/')
def hello():
    expr = 2*x**2+3*x+1
    obj = {
        "simplify": str(simplify(expr)),
        "factor": str(factor(expr)),
        "solve": str(solve(expr))
    }
    # print(obj["factor"])
    return json.dumps(obj)


@app.route('/getSolution', methods=['GET'])
def getSolution():
    data = request.get_json()
    expr=data["expr"]
    obj = {
        "simplify": str(simplify(expr)),
        "factor": str(factor(expr)),
        "solve": str(solve(expr))
    }
    # print(obj["factor"])
    return json.dumps(obj),200;
