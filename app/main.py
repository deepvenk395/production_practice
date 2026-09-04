from fastapi import FastAPI

app = FastAPI(
    title="Production DevSecOps Platform",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "fastapi",
    }


@app.get("/ready")
def ready():
    return {
        "status": "ready",
        "service": "fastapi",
    }


@app.get("/version")
def version():
    return {
        "version": "0.1.0",
        "environment": "development",
    }
