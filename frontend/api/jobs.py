import httpx

from frontend.api.schemas import CorrectJob


class JobsApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[CorrectJob]:
        response = httpx.get(f'{self.url}/api/v1/jobs/')
        response.raise_for_status()

        return [CorrectJob(**job) for job in response.json()]

    def get_for_company(self, uid) -> list[CorrectJob]:
        response = httpx.get(f'{self.url}/api/v1/companies/{uid}/jobs/')
        response.raise_for_status()

        return [CorrectJob(**job) for job in response.json()]
