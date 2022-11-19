from flask import Flask, render_template
from random import choice
from random import randint

app = Flask(__name__)

@app.route("/rps/<player>")
def rps(player):
    weapons = ["rock", "paper", "scissors"]
    phrases = ["It's a draw", "Computer wins!", "Player wins!"]
    computer = choice(weapons)
    if player == computer:
        return render_template('rps.html', player=player, computer=computer, phrases=phrases[0])
    elif computer == "rock" and player == "scissors":
        return render_template('rps.html', player=player, computer=computer, phrases=phrases[1])
    elif computer == "paper" and player == "rock":
        return render_template('rps.html', player=player, computer=computer, phrases=phrases[1])
    elif computer == "scissors" and player == "paper":
        return render_template('rps.html', player=player, computer=computer, phrases=phrases[1])
    elif computer == "scissors" and player == "rock":
        return render_template('rps.html', player=player, computer=computer, phrases=phrases[2])
    elif computer == "rock" and player == "paper":
        return render_template('rps.html', player=player, computer=computer, phrases=phrases[2])
    elif computer == "paper" and player == "scissors":
        return render_template('rps.html', player=player, computer=computer, phrases=phrases[2])

@app.route("/could_it_be_me/<int:num_lines>")
def send_lotto_numbers(num_lines):
    lines = []
    for j in range(0, num_lines):
        line = []
        for i in range(0, 6):
            n = randint(1, 47)
            line.append(n)  
        lines.append(line)
    return render_template("lotto.html", lines=lines)

