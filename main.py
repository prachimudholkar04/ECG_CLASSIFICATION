from fastapi import FastAPI


app = FastAPI()

@app.get("/greet")
def read_greet(name: str):
    if not name:
        raise HTTPException(status_code=400, detail="Name must be provided.")
    return {"greeting": f"Hello, {name}!"}
