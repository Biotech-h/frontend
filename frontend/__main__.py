from flask import Flask, render_template

from frontend.api.companies import CompaniesApi
from frontend.config import config

companies_api = CompaniesApi(config.backend.url)

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Biotech-h'
    return render_template('index.html', page_title=title)


@app.get('/companies')
def get_all_companies():
    companies = companies_api.get_all()

    return render_template('companies.html', page_title='Список компаний', companies=companies)


if __name__ == '__main__':
    app.run(host=config.server.host, port=config.server.port)
