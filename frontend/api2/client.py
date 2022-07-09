from frontend.api.companies import CompaniesApi
from frontend.api.jobs import JobsApi
from frontend.config import config


class ApiClient:

    def __init__(self, url: str) -> None:
        self.companies = CompaniesApi(url)
        self.jobs = JobsApi(url)


client = ApiClient(config.backend.url)
