from fastapi import FastAPI
import subprocess

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.get("/command")
def command():
    user_input = "ls"

    result = subprocess.run(
        user_input,
        shell=False,
        capture_output=True,
        text=True
    )

    return {"output": result.stdout}
