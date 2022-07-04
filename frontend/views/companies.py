from flask import Blueprint, render_template

from frontend.api.client import client

routes = Blueprint('companies', __name__)


@routes.get('/companies')
def get_all():
    companies = client.companies.get_all()

    return render_template('companies.html', page_title='Список компаний', companies=companies)
