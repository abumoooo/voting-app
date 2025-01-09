from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def results():
    kot_votes = int(redis_client.get('kot') or 0)
    pies_votes = int(redis_client.get('pies') or 0)
    return f'''
        <div style="text-align: center; font-family: Arial, sans-serif; padding: 20px;">
            <h1>Wyniki głosowania</h1>
            <p style="font-size: 20px;">🐱 Kot: <b>{kot_votes}</b></p>
            <p style="font-size: 20px;">🐶 Pies: <b>{pies_votes}</b></p>
            <a href="/" style="text-decoration: none; font-size: 18px; color: blue;">Powrót do głosowania</a>
        </div>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
