import os
from flask import Flask, request, jsonify, json

app = Flask("Teste")


@app.route("/")
def home():
    return {"ola":"mundo"}

@app.route("/<operacao>&<int:num1>&<int:num2>")
def conta(operacao,num1,num2):
    result = 0
    if operacao.upper() == "SOMA":
        result = num1 + num2
    elif operacao.upper() == "SUBTRAI":
        result = num1 - num2
    elif operacao.upper() == "DIVIDE":
        result = num1 / num2
    else:
        result = "invalido"
    return {'resultado' : result}


app.run(port='8000')
