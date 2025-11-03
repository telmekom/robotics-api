import os
from fastapi import Depends, FastAPI
from routers import analysis, maps, shops, robots
import requests
from shared.pudu_api_helper import HACKATHON_API_KEY, build_headers_with_hmac, header_scheme
from dotenv import load_dotenv

load_dotenv()  


app = FastAPI()


app.include_router(shops.router)
app.include_router(robots.router)
app.include_router(maps.router)
app.include_router(analysis.router)

@app.get("/healthcheck", description="Basic server availability check")
def health_check(key: str = Depends(header_scheme)):
    if (key != HACKATHON_API_KEY):
        return {"code": 401, "message": "Unauthorized: API-Key not valid"}
        
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
