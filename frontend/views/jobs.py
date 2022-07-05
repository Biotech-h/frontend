from flask import Blueprint, render_template

from frontend.api.client import client

routes = Blueprint('jobs', __name__)


@routes.get('/jobs')
def get_all():
    jobs = client.jobs.get_all()

    return render_template('jobs.html', page_title='Список вакансий', jobs=jobs)
