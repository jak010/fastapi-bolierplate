from fastapi import FastAPI

from src.controller import controller_router


class BoilerPlateApplication:
    app = FastAPI()

    def __call__(self, *args, **kwargs):
        self.app.include_router(controller_router)

        return self.app


application = BoilerPlateApplication()
