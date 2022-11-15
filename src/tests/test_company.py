import sys

import pytest

sys.path.append("..")

class TestCompany:
  @pytest.mark.asyncio
  async def test_company_validate_payload(self):
    from exceptions.invalidPayloadException import InvalidPayloadException
    from service.companyService import CompanyService
    
    data = {
      'name': 'Test Company',
      'email': 'test@test.com',
      'password': '123456',
      'password_confirmation': '123456',
    }
    
    data_list = []
    for i in data:
      data_copy = data.copy()
      data_copy.pop(i)
      company = CompanyService()
      
      try:
        await company.create(data_copy)
      except InvalidPayloadException as e:
        data_list.append(e.message)
    
    data_copy = data.copy()
    data_copy['password_confirmation'] = 'asd'
    
    try:
      company = CompanyService()
      await company.create(data_copy)
    except InvalidPayloadException as e:
      data_list.append(e.message)
    
    assert data_list == ['Missing field name', 
                         'Missing field email', 
                         'Missing field password', 
                         'Missing field password_confirmation', 
                         'Password and password confirmation do not match']

  