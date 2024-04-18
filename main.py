from flask import Flask, request, render_template, redirect, url_for, session, jsonify

app = Flask(__name__)  

@app.route('/<ratings>', methods =["GET", "POST"])
def save(ratings):
    if request.method == "POST":
        file = open('test.txt', 'w')
        file.writelines(ratings)
        file.close()
        return 'done'
    if request.method == "GET":
        file = open('test.txt', 'r')
        return file.readlines()
