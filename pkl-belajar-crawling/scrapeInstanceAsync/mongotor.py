import asyncio, motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client.ScrapedPlat
col = db.ScrapedPlat

async def do_insert(data):
    result = db.ScrapedPlat.insert_many(data) 
    print (result)