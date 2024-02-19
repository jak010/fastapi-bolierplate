from fastapi import FastAPI


class BoilerPlateApplication:
    app = FastAPI()

    def __call__(self, *args, **kwargs):
        return self.app


application = BoilerPlateApplication
