

from fastapi import FastAPI
from routes.genex_router import gene_router
from routes.internal_router import internal_routes
app = FastAPI()


app.include_router(internal_routes)
app.include_router(gene_router)