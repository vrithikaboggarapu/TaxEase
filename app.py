from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'devops_2025'

