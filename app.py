from flask import Flask, render_template, request, jsonify
import chess

app = Flask(__name__)
board = chess.Board()

@app.route('/')
def index():
    return render_template('index.html', board=board.fen())

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    move = data.get('move')
    try:
        board.push_san(move)
        return jsonify({'fen': board.fen(), 'status': 'ok'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'})

if __name__ == '__main__':
    app.run(debug=True)
