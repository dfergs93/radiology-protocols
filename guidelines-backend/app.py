from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os

from guideline_tools import (
    fleischner_calculator,
    adrenal_washout_calculator,
    GUIDELINE_TOOLS,
)

app = FastAPI()

ALLOWED_ORIGINS = [
    "http://localhost:8002",
    "http://127.0.0.1:8002",
    "https://dfergs93.github.io",
    "https://dfergs93.github.io/guidelines-manager/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FleischnerRequest(BaseModel):
    size_mm: float
    nodule_type: str  # solid | part-solid | ground-glass
    patient_risk: str  # low | high
    multiplicity: str  # single | multiple


class AdrenalWashoutRequest(BaseModel):
    unenhanced_hu: float
    venous_hu: float
    delayed_hu: float


@app.post("/api/fleischner")
def fleischner(request: FleischnerRequest):
    return fleischner_calculator(
        size_mm=request.size_mm,
        nodule_type=request.nodule_type,
        patient_risk=request.patient_risk,
        multiplicity=request.multiplicity,
    )


@app.post("/api/adrenal-washout")
def adrenal_washout(request: AdrenalWashoutRequest):
    return adrenal_washout_calculator(
        unenhanced_hu=request.unenhanced_hu,
        venous_hu=request.venous_hu,
        delayed_hu=request.delayed_hu,
    )


@app.get("/api/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)
