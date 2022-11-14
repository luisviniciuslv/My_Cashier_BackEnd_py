import json
from flask import Blueprint, jsonify, request
from src.exceptions.companyAlreadyExists import CompanyAlreadyExists
from src.exceptions.invalidPayloadException import InvalidPayloadException
from src.service.companyService import CompanyService
company = Blueprint('company', __name__, url_prefix='/company')
@company.route('/',methods=['GET'])
def index():
  return jsonify({'message': 'Hello World'}), 200

@company.route('/',methods=['POST'])
async def create():
  data = request.get_json()
  try:
    company = CompanyService()
    await company.create(data)
    return jsonify({'message': 'Company created'}), 201
  
  except InvalidPayloadException as e:
    return jsonify({'message': e.message}), 400
  
  except CompanyAlreadyExists as e:
    return jsonify({'message': e.message}), 400