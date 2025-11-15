from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient

import config

from ..logging import LOGGER

LOGGER(__name__).info("⏳ Establishing a secure link to your MongoDB database...")
try:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.Auput
    pymongodb = _mongo_sync_.Auput
    LOGGER(__name__).info("✅ Successfully connected to MongoDB. All systems are ready!")
except:
    LOGGER(__name__).error("❌ MongoDB connection failed!")
    exit()
