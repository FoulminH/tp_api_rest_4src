from .status import router as status_router
from .query import router as query_router

all_routers = [
    status_router,
    query_router
]