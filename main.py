

from fastapi import FastAPI
from routes.genex_router import gene_router
from routes.internal_router import internal_routes
from routes.gene_db_router import gene_db_router
from pymongo import MongoClient, ASCENDING
from config import config
app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    
    client = MongoClient(config["MONGO_URI_GENES"])
    database = client["gene-database"]
    app.state.db_client = client
    app.state.db = database
    app.state.gene_collection = database["genes"]
    app.state.gene_collection.create_index([("name", ASCENDING)], unique=True)
    print("Connected to MongoDB (PyMongo)")


@app.on_event("shutdown")
def shutdown_db_client():
    app.state.db_client.close()

    # 2. Disconnect MongoEngine (optional, but good practice)
    print("Pymongo connection closed.")







app.include_router(internal_routes)
app.include_router(gene_router)
app.include_router(gene_db_router)