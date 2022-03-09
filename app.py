from flask import Flask,redirect,url_for,render_template,request
import requests
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        def toFer(abc):
            final_feelsLike = (abc - 273.15) * (9 / 5) + 32
            return round(final_feelsLike, 2)
        city = request.form['city']
        apikey = "e408964eb2206f1573c77832841e6b11"
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apikey
        degree_sign = u"\N{DEGREE SIGN}"
        response = requests.get(url)
        data = response.json()
        desc = data['weather'][0]['description']
        feelsLike = toFer(data['main']['feels_like'])
        mintemp = toFer(data['main']['temp_min'])
        maxtemp = toFer(data['main']['temp_max'])
    return render_template('ourResponse.html', desc=desc,mintemp=mintemp,feelsLike=feelsLike,maxtemp=maxtemp,city=city,degree_sign=degree_sign)




if __name__ == '__main__':
    app.run()
