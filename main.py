from flask import Flask, request, render_template, redirect, url_for, session, jsonify

app = Flask(__name__)  

@app.route('/<ratings>', methods =["GET", "POST"])
def save(ratings):
    if request.method == "POST":
        file = open('ratings.txt', 'w')
        file.writelines(ratings)
        file.close()
        return 'done'
    if request.method == "GET":
        file = open('ratings.txt', 'r')
        return file.readlines()
