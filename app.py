from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    weight = float(request.form['weight'])
    origin = request.form['origin']
    destination = request.form['destination']

    sea = round(weight * 0.01, 2)
    rail = round(weight * 0.03, 2)
    air = round(weight * 0.5, 2)
    saving = round(air - sea, 2)

    return render_template('result.html',
        origin=origin,
        destination=destination,
        weight=weight,
        sea=sea,
        rail=rail,
        air=air,
        saving=saving)

if __name__ == '__main__':
    app.run(debug=True)