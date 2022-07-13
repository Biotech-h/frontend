from flask import Blueprint, render_template

from frontend.api.client import client
from frontend.api.schemas import CorrectCompany, CorrectJob

routes = Blueprint('jobs', __name__)


def to_model(job: CorrectJob, companies: dict[int, CorrectCompany]) -> tuple[CorrectJob, str]:
    company = companies[job.company_uid]
    company_name = company.name

    return job, company_name


def get_companies_map():
    companies = client.companies.get_all()

    return {company.uid: company for company in companies}


@routes.get('/jobs')
def get_all():
    jobs = client.jobs.get_all()
    companies = get_companies_map()
    models = [to_model(job, companies) for job in jobs]

    return render_template(
        'jobs.html',
        page_title='Все вакансии',
        jobs=models,
        companies=list(companies.values()),
    )
