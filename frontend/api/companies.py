from typing import Any

import httpx


class CompaniesApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[dict[str, Any]]:
        response = httpx.get(f'{self.url}/api/v1/companies/')
        response.raise_for_status()

        return response.json()
