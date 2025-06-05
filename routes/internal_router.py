from fastapi import APIRouter, Depends
from utils.auth import verify_token

internal_routes= APIRouter(
    prefix="/internal",
    tags=["internal"],
    
)




@internal_routes.get("/restricted", dependencies=[Depends(verify_token)])
def restricted():
    """
    Internal route for testing purposes.
    This route is protected by token authentication and returns a simple message 
    """

    return {"message": "Access granted", "status": "success"}



@internal_routes.get("/restricted2", dependencies=[Depends(verify_token)])
def restricted2():
    """
    Internal route for testing purposes.
    This route is protected by token authentication and returns a simple message 
    """

    return {"message": "Access granted to the second restricted route", "status": "success"}