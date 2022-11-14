# import type ID mongodb
import certifi
from bson.objectid import ObjectId
from dotenv import load_dotenv
import pymongo 
from pymongo.server_api import ServerApi
load_dotenv()
import os

ca = certifi.where()
client = pymongo.MongoClient(os.getenv('DATABASE_CONNECTION'), server_api=ServerApi('1'))
db = client['MyCashier']
collection = db['Company']

class CompanyRepository:
  async def create(self, data: dict):
    collection.insert_one(data)
    
  async def find_by_id(self, id: ObjectId):
    return collection.find
  
  async def find_by_email(self, email: str):
    try:
      return collection.find_one({'email': email})
    except:
      return None
