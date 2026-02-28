from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello Kitty - Princess Merry</title>
        <style>
            body {
                background: linear-gradient(135deg, #ffb6c1, #ffc0cb);
                font-family: 'Comic Sans MS', cursive, sans-serif;
                text-align: center;
                padding: 50px;
            }
            .kitty-container {
                background: white;
                border-radius: 50px;
                padding: 30px;
                box-shadow: 0 10px 30px rgba(255, 105, 180, 0.5);
                max-width: 600px;
                margin: 0 auto;
                border: 5px solid #ff69b4;
            }
            h1 {
                color: #ff1493;
                font-size: 3em;
                text-shadow: 3px 3px 0 #ffe4e1;
            }
            .princess {
                color: #ff69b4;
                font-size: 2em;
            }
            .kitty-emoji {
                font-size: 8em;
                margin: 20px;
                animation: bounce 2s infinite;
            }
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-20px); }
            }
            .heart {
                color: #ff1493;
                font-size: 2em;
            }
            .pipeline-info {
                background: #fff0f5;
                border-radius: 30px;
                padding: 15px;
                margin-top: 20px;
                border: 2px solid #ffb6c1;
            }
        </style>
    </head>
    <body>
        <div class="kitty-container">
            <div class="kitty-emoji">🐱🎀</div>
            <h1>Hello Kitty!</h1>
            <div class="princess">✨ Princess Merry ✨</div>
            <div class="heart">❤️ 😺 ❤️</div>
            <div class="pipeline-info">
                <p>🌸 Bienvenue dans mon pipeline DevOps tout mignon 🌸</p>
                <p>Version: 1.0</p>
                <p>Status: 🚀 En pleine forme !</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
