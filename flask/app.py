import sys
from flask import Flask, render_template, jsonify, url_for, request, redirect, flash, session

app = Flask(__name__)

@app.route('/')
def greet():
    return "welcome"

@app.route('/bin_to_dec/<int:binary>')
def binaryToDecimal(binary):     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return str(decimal)

@app.route('/dec_to_bin/<int:n>')
def decimalToBinary(n):
     return "{0:b}".format(int(n))
    
if __name__ == '__main__':
    app.run(debug=True)