# Necessary Imports
from fastapi import FastAPI                   # The main FastAPI import
from fastapi.responses import HTMLResponse    # Used for returning HTML responses
from fastapi.staticfiles import StaticFiles   # Used for serving static files
import uvicorn                                # Used for running the app
from fastapi.responses import RedirectResponse
from fastapi import Request, Form


# Configuration
app = FastAPI()                   # Specify the "app" that will run the routing
# Mount the static directory
app.mount("/public", StaticFiles(directory="public"), name="public")


# Example route: return a static HTML page
@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("index.html") as html:
        return HTMLResponse(content=html.read())

# Example route: return a static HTML page
@app.get("/case_studies", response_class=HTMLResponse)
def get_case_studies() -> HTMLResponse:
    with open("case_studies.html") as html:
        return HTMLResponse(content=html.read())

# Example route: return a static HTML page 
      
@app.get("/schedule", response_class=HTMLResponse)
def get_schedule() -> HTMLResponse:
    with open("schedule.html") as html:
        return HTMLResponse(content=html.read())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)