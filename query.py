from fastapi import FastAPI
app = FastAPI ()
@app.get("/suma/")
def suma(a: int, b:int):
    return {"Resultado": a + b}
