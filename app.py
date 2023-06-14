import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from router import router

app = FastAPI()

app.include_router(
    router
)

@app.get("/")
async def root(request: Request) -> HTMLResponse:
    return HTMLResponse(
        content="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo RestAPI</title>
</head>
<body>
    please visit <a href="http://localhost:8080/docs">docs</a>
    <p>This site is not finished yet!</p>
</body>
</html>
        """
    )

if __name__ == "__main__":
    uvicorn.run(
        app="app:app",
        host="localhost",
        port=8080,
        reload=True,
        workers=2
    )
