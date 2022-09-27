from flask import Flask, render_template,request
import requests

app=Flask('weather')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method =='POST':
        data = request.form.get('weathers')
        print(data)
        url = f'https://api.openweathermap.org/data/2.5/weather?q={data}&appid=0c1f63f761e0caf78712ec7b00736ec0'
        print(url)
        api_data = requests.get(url)
        python_dict = api_data.json()
        print(python_dict)
        tempe =python_dict['main']['temp']
        vis =python_dict['visibility']
        hum =python_dict['main']['humidity']
        pre =python_dict['main']['pressure']
        win =python_dict['wind']['speed']
        return render_template('index.html',  data = data ,tempe = tempe,hum=hum,vis=vis,pre=pre,win=win)
    else:

        return render_template('index.html')

app.run()






