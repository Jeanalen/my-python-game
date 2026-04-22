from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# Game Logic Functions
choice_map = {"rock": "rock", "paper": "paper", "scissors": "scissors"}
choices = ["rock", "paper", "scissors"]

def determine_winner(player, computer):
    if player == computer: return "tie"
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
       (player == "paper" and computer == "rock"):
        return "win"
    return "lose"

# Simple HTML Template to show the game in the browser
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Rock Paper Scissors</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; }
        button { font-size: 20px; padding: 10px 20px; cursor: pointer; margin: 5px; }
        .result { font-weight: bold; font-size: 24px; color: blue; }
    </style>
</head>
<body>
    <h1>Rock, Paper, Scissors!</h1>
    <p>Choose your move:</p>
    <form method="POST">
        <button name="choice" value="rock">Rock</button>
        <button name="choice" value="paper">Paper</button>
        <button name="choice" value="scissors">Scissors</button>
    </form>
    
    {% if player_choice %}
        <div class="result">
            <p>You chose: {{ player_choice }}</p>
            <p>Computer chose: {{ computer_choice }}</p>
            <h2>Result: {{ result }}</h2>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        player_choice = request.form.get('choice')
        computer_choice = random.choice(choices)
        result = determine_winner(player_choice, computer_choice)
        return render_template_string(HTML_TEMPLATE, 
                                     player_choice=player_choice, 
                                     computer_choice=computer_choice, 
                                     result=result)
    return render_template_string(HTML_TEMPLATE)

# This is required for Vercel
app.debug = True
