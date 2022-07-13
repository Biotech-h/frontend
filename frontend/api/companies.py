import httpx

from frontend.api.schemas import CorrectCompany


class CompaniesApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[CorrectCompany]:
        response = httpx.get(f'{self.url}/api/v1/companies/')
        response.raise_for_status()

        return [CorrectCompany(**company) for company in response.json()]
