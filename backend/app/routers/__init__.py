from fastapi import APIRouter

from . import api, auth, page, user

router = APIRouter(prefix="/api")
router.include_router(auth.router)
router.include_router(user.router)
router.include_router(api.router)
router.include_router(page.router)
