from flask import Flask, request, render_template, jsonify
import random

app = Flask(__name__)

# Define game options
options = ("rock", "paper", "scissors")

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML frontend

@app.route('/play', methods=['POST'])
def play_game():
    data = request.get_json()
    player_choice = data.get('choice', '').lower().strip()

    # Validate player's choice
    if player_choice not in options:
        return jsonify({'message': 'Invalid choice! Please choose rock, paper, or scissors.'}), 400

    computer_choice = random.choice(options)

    # Determine result
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    return jsonify({
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
