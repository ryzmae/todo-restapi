import uvicorn

from fastapi import FastAPI

from router import router

app = FastAPI()

app.include_router(
    router
)

if __name__ == "__main__":
    uvicorn.run(
        app="app:app",
        host="localhost",
        port=8080,
        reload=True,
        workers=2
    )
