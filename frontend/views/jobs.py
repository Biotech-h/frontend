from flask import Blueprint, render_template

from frontend.api.jobs import JobsApi
from frontend.config import config

routes = Blueprint('jobs', __name__)

jobs_api = JobsApi(config.backend.url)


@routes.get('/jobs')
def get_all():
    jobs = jobs_api.get_all()

    return render_template('jobs.html', page_title='Список вакансий', jobs=jobs)
