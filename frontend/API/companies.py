import httpx

class CompaniesApi:

    def __init__(self):
        self = self
        
    def get_all():
        response = httpx.get('http://192.168.1.6:8080/api/v1/companies/')
        response.raise_for_status()
        
        return response.json()
        