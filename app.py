from flask import Flask, render_template
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
import os

app = Flask(__name__)

@app.route('/')
def index():
    csv_path = os.path.join(os.path.dirname(__file__), 'data.csv')
    df = pd.read_csv(csv_path)

    df = df.sort_values(by='number', ascending=False)

    x = df['name']
    y = df['number']

    trace = go.Bar(x=x, y=y, name='数値')
    layout = go.Layout(title='名前ごとの数値棒グラフ', xaxis=dict(title='名前'), yaxis=dict(title='数値'))
    fig = go.Figure(data=[trace], layout=layout)
    graph_html = pyo.plot(fig, output_type='div')

    return render_template("index.html", graph_html=graph_html)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



