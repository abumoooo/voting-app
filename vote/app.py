from flask import Flask, request
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vote = request.form['vote']
        redis_client.incr(vote)
        return '''
            <h1>Dziękujemy za głosowanie!</h1>
            <p>Twój głos został zapisany.</p>
            <a href="/">Powrót do głosowania</a>
        '''
    return '''
        <div style="text-align: center; font-family: Arial, sans-serif; padding: 20px;">
            <h1>Głosowanie</h1>
            <form method="post" style="display: inline-block;">
                <button type="submit" name="vote" value="kot" style="padding: 10px 20px; margin: 10px; font-size: 18px;">Głosuj na kota</button>
                <button type="submit" name="vote" value="pies" style="padding: 10px 20px; margin: 10px; font-size: 18px;">Głosuj na psa</button>
            </form>
        </div>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
