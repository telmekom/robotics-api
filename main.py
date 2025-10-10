import os
from fastapi import FastAPI
from routers import shops, robots
import requests
from shared.pudu_api_helper import build_headers_with_hmac
from dotenv import load_dotenv
load_dotenv()  


app = FastAPI()
app.include_router(shops.router)
app.include_router(robots.router)

@app.get("/healthcheck", description="Basic server availability check")
def health_check():
    try:
        request_data = {
            "url": f'{os.getenv("PUDU_BASE_URL")}/pudu-entry/data-open-platform-service/v1/api/healthCheck',
            "accept": 'application/json',
            "content_type": 'application/json',
            "method": 'GET',
            "app_key" : os.getenv("API_APP_KEY"),
            "secret_key": os.getenv("API_APP_SECRET"),
        }
        hmac_headers = build_headers_with_hmac(**request_data)
        response = requests.get(request_data["url"], headers=hmac_headers)
            
        if response.status_code == 200:
            return response.json()
        else:
            # [TODO] better error info
            return { response.text}
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}
