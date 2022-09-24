from flask import Flask
app = Flask(__name__)

@app.route("/explain")
def get():
    return "The goal of this game is to create an insurance plan and avoid the obstacles throughout the game. There" \
           " will be obstacles throughout the course of the game and the goal is to get the best net balance from the " \
           "game possible. There will be 10 years to go through the game and each year may have an obstacle that might " \
           "hinder you. Try your best to get through the game with the least amount of money to pay! Good luck!"




