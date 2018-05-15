from flask import Flask, render_template, request, redirect
from downloader import Downloader
import time

app = Flask(__name__)

speeds = []

@app.route('/')
def index():
    speeds[:] = []
    return render_template('index.html')


@app.route('/', methods=['POST'])
def search():
    url = request.form['url']
    threads = [1, 2, 4, 8, 16]

    for thread in threads:
        start_time = time.clock()
        down = Downloader(url=url, num=thread)
        # 执行run方法
        down.run()
        spend = time.clock() - start_time
        speed = round(down.total / spend / 1024, 5)
        print(speed)
        speeds.append(speed)

    print(speeds)
    return redirect('/threadmap')


@app.route('/threadmap')
def data():
    return render_template('threadmap.html', speeds=speeds)


if __name__ == '__main__':
    app.run(debug=True)
