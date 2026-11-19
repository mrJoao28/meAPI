from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/name')
def give_name():
    return "<p> João Felipe</p>"

@app.route("/age")
def give_age():
    age = datetime.now().year - 2008
    return f"<p> {age} years old</p>"

@app.route("/sport")
def give_sport():
    return "<p> Swimming Ski</p>"


@app.route("/console")
def give_console():
    return "<p> Xbox One</p>"

@app.route("/podcast")
def give_podcast():
    return "<p> Joe Rogan Experience</p>"

@app.route("/movie")
def give_movie():
    return "<p>  Interstellar </p>"

@app.route("/series")
def give_series():
    return "<p> Peaky Blinders </p>"

@app.route("/game")
def give_game():
    return "<p> Forza Horizon 4 </p>"

@app.route("/food")
def give_food():
    return "<p> Chateaubriand </p>"

@app.route("/vacations")
def give_vacations():
    return "<p> Fortaleza Belem Curitiba São Paulo BC Floripa Gramado Porto Alegre </p>"

@app.route("/girlfriend")
def give_girlfriend():
    return "<p> No </p>"

@app.route("/dream")
def give_dream():
    return "<p> almost 1 billion dollars on assets </p>"

@app.route("/airplane")
def give_airplane():
    return "<p> Airbus A380 </p>"

@app.route("/dream_car")
def give_dream_car():
    return "<p> Bugatti Tourbillon </p>"

@app.route("/country")
def give_country():
    return "<p> Brazil </p>"

@app.route("/city")
def give_city():
    return "<p> Manaus </p>"

@app.route("/favorite_song")
def give_favorite_song():
    return "<p> My Way </p>"

@app.route("/color")
def give_color():
    return "<p> Black </p>"

@app.route("/computer")
def give_computer():
    return "<p> MacBook Pro </p>"

@app.route("/phone")
def give_phone():
    return "<p> Samsung M53 </p>"

@app.route("/job")
def give_job():
    return "<p> Create and Sale </p>"

@app.route("/college")
def give_college():
    return "<p> UEA </p>"

@app.route("/degree")
def give_degree():
    return "<p> Computer Engineering </p>"

@app.route("/investor")
def give_investor():
    return "<p> Bill ALckman </p>"

@app.route("/entrepreneur")
def give_entrepreneur():
    return "<p> Steve Jobs </p>"

@app.route("/philosopher")
def give_philosopher():
    return "<p> Santo Agostinho </p>"

