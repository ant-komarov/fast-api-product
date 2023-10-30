from fastapi import FastAPI

import router


app = FastAPI()

app.include_router(router.router_v1)


@app.get("/")
def root() -> dict:
    return {"message": "Wellcome to product app"}
