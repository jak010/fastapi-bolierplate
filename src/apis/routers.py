from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

router = APIRouter(tags=['API'], prefix="/api/v1")


@router.get("")
def hello_world():
    return JSONResponse(status_code=200, content={})
