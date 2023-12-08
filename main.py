from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bounty(score):
    if 1 <= score < 3:
        return round((score - 1) / (3 - 1) * (250 - 50) + 50)
    elif 3 <= score < 6:
        return round((score - 3) / (6 - 3) * (600 - 251) + 251)
    elif 6 <= score < 9:
        return round((score - 6) / (9 - 6) * (1200 - 601) + 601)
    elif 9 <= score <= 10:
        return round((score - 9) / (10 - 9) * (5000 - 1201) + 1201)
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            input_score = float(request.form['score'])
            if 1 <= input_score <= 10:
                bounty = calculate_bounty(input_score)
                if bounty is not None:
                    return render_template('result.html', bounty=bounty)
                else:
                    return render_template('index.html', error="Score is outside the defined ranges.")
            else:
                return render_template('index.html', error="Please enter a valid score between 1 and 10.")
        except ValueError:
            return render_template('index.html', error="Please enter a valid numerical score.")
    return render_template('index.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)
