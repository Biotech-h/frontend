from flask import Blueprint, render_template, request

from frontend.api.client import client

routes = Blueprint('companies', __name__)


@routes.get('/companies')
def get_all():
    companies = client.companies.get_all()

    return render_template('companies.html', page_title='Все компании', companies=companies)


@routes.get('/companies/<int:uid>/jobs')
def get_for_company(uid):
    name = request.args['name']
    jobs = client.jobs.get_for_company(uid)

    return render_template(
        'jobs_by_company.html',
        jobs=jobs,
        company_name=name,
        page_title=f'Все вакансии {name}',
    )
