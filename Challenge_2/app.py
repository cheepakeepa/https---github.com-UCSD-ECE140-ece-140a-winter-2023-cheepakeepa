from fastapi import FastAPI, Request, Form
from fastapi.responses import Response
from fastapi.responses import HTMLResponse
import uvicorn
from urllib.request import urlopen
import json

app = FastAPI()


# Example route: return a HTML page
@app.get("/", response_class=HTMLResponse)

def get_html() -> HTMLResponse:
    with open("index.html") as html:
        return HTMLResponse(content=html.read())

@app.get("/page", response_class=HTMLResponse)

def get_html() -> HTMLResponse:
    with open("page.html") as html:
        return HTMLResponse(content=html.read())


# Example route: returns JSON
@app.post("/stock")
def post_form(request: Request, symbol: str = Form(...)):
    # define API key
    """
    INSTANTIATE THIS VARIABLE WITH YOUR API KEY
    """
    api_key = "5092e99c6465e10cc00a10e60f36d3dd"
    # create url link
    url_1 = 'https://financialmodelingprep.com/api/v3/profile/' + symbol1 + '?apikey=' + api_key


    # store the response of URL
    response1 = urlopen(url_1)


    # store the JSON response from URL
    stock_1_json = json.loads(response.read())
    url_2 = 'https://financialmodelingprep.com/api/v3/profile/' + symbol2 + '?apikey=' + api_key


    # store the response of URL
    response2 = urlopen(url_2)


    # store the JSON response from URL
    stock_2_json = json.loads(response.read())
    url_3 = 'https://financialmodelingprep.com/api/v3/profile/' + symbol3 + '?apikey=' + api_key


    # store the response of URL
    response3 = urlopen(url_3)


    # store the JSON response from URL
    stock_3_json = json.loads(response.read())


    # check if empty thus invalid stock symbol
    if len(data_json) == 0:
        return {}


    # return json data
    return data_json
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)
