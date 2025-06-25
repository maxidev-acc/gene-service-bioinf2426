from fastapi import APIRouter, Request, HTTPException, Depends, Body
from models.gene import GeneModel, GeneFields, DeletionModel, InsertionModel, PointMutationModel


gene_db_router = APIRouter(prefix="/genes", tags=["genes"])#, dependencies=[Depends(verify_token)])




@gene_db_router.get("/all")
def find_all(request: Request):
    try:
        cursor = request.app.state.gene_collection.find()
        genes = []
        for gene in cursor:
            gene["_id"] = str(gene["_id"])  # Convert ObjectId to string
            genes.append(gene)
        return {"all": genes}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@gene_db_router.get("/get/{gene_name}")
def read_gene(gene_name: str, request: Request):
    try:
        gene = request.app.state.gene_collection.find_one({"name": gene_name})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")
    if not gene:
        raise HTTPException(status_code=404, detail="Gene not found")
    gene["_id"] = str(gene["_id"])
    #print(gene)
    return gene



@gene_db_router.put("/mutations/pointmutation/add/{gene_name}")
def update_gene_add_pointmutation(gene_name: str, mutation: PointMutationModel  , request: Request):

    result = request.app.state.gene_collection.update_one(
        {"name": gene_name},
        {"$push": {"mutations": mutation.model_dump()}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Gene not found")
    updated_gene = request.app.state.gene_collection.find_one({"name": gene_name})
    updated_gene["_id"] = str(updated_gene["_id"])
    return updated_gene


@gene_db_router.put("/mutations/insertion/add/{gene_name}")
def update_gene_add_insertion(gene_name: str, mutation: InsertionModel  , request: Request):

    result = request.app.state.gene_collection.update_one(
        {"name": gene_name},
        {"$push": {"mutations": mutation.model_dump()}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Gene not found")
    updated_gene = request.app.state.gene_collection.find_one({"name": gene_name})
    updated_gene["_id"] = str(updated_gene["_id"])
    return updated_gene



@gene_db_router.put("/mutations/deletion/add/{gene_name}")
def update_gene_add_deletion(gene_name: str, mutation: DeletionModel  , request: Request):

    result = request.app.state.gene_collection.update_one(
        {"name": gene_name},
        {"$push": {"mutations": mutation.model_dump()}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Gene not found")
    updated_gene = request.app.state.gene_collection.find_one({"name": gene_name})
    updated_gene["_id"] = str(updated_gene["_id"])
    return updated_gene




















@gene_db_router.post("/add")
def create_gene(gene: GeneModel, request: Request):
    
    try:
        gene_dict = gene.model_dump()
        result = request.app.state.gene_collection.insert_one(gene_dict)
        gene_dict["_id"] = str(result.inserted_id)
        return gene_dict
    except Exception:
        raise HTTPException(status_code=400, detail="Gene already in database")







@gene_db_router.delete("/delete/{gene_name}")
def delete_gene(gene_name: str, request: Request):
    result = request.app.state.gene_collection.delete_one({"name": gene_name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Gene not found")
    return {"message": "Gene deleted successfully"}