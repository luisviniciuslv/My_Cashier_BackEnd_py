import bcrypt
from src.exceptions.companyAlreadyExists import CompanyAlreadyExists
from src.repository.companyRepository import CompanyRepository
from src.service.validations.companyCreate import validatePayload


class CompanyService:
  def __init__(self):
    self.repository = CompanyRepository()
  
  async def create(self, data: dict):
    validatePayload(data)
    email = data['email']
    found_company = await self.repository.find_by_email(str(email))
    
    if found_company:
      raise CompanyAlreadyExists('Company email already exists')
    
    salt = bcrypt.gensalt(rounds=10)
    data['password'] =  bcrypt.hashpw(data['password'].encode('utf-8'), salt)

    return await self.repository.create(data)
