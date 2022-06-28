from flask import Flask, render_template

from frontend.config import config
from frontend.views import companies, jobs

app = Flask(__name__)
app.register_blueprint(companies.routes, url_prefix='/')
app.register_blueprint(jobs.routes, url_prefix='/')


@app.route('/')
def index():
    title = 'Biotech-h'
    return render_template('index.html', page_title=title)


if __name__ == '__main__':
    app.run(host=config.server.host, port=config.server.port)
