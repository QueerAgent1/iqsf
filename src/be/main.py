from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from .models import SafetyReport

app = FastAPI()

# Allow SvelteKit (default: localhost:5173) to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust to your FE port/domain as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory "DB" for demo
safety_reports = []

@app.post("/reports/", response_model=SafetyReport)
def create_report(report: SafetyReport):
    report.id = len(safety_reports) + 1
    safety_reports.append(report)
    return report

@app.get("/reports/", response_model=List[SafetyReport])
def list_reports():
    return safety_reports

@app.get("/reports/{report_id}", response_model=SafetyReport)
def get_report(report_id: int):
    for r in safety_reports:
        if r.id == report_id:
            return r
    raise HTTPException(status_code=404, detail="Report not found")