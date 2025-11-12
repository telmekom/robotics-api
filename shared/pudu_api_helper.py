import base64
import datetime
from enum import Enum
import hmac
import hashlib
import requests

from urllib.parse import urlencode, urlparse, unquote
import os
from dotenv import load_dotenv
from fastapi.security import APIKeyHeader
load_dotenv()  

HACKATHON_API_KEY = os.getenv("HACKATHON_API_KEY")
header_scheme = APIKeyHeader(name="x-key")


class EntityType(Enum):
    ROBOT = "ROBOT"
    MAP = "MAP"
    SHOP = "SHOP"

def is_allowed_id(type: EntityType, id: str):
    WHITELISTED_IDS = os.getenv(f"{type.value}_IDS").split(",")
    if id not in WHITELISTED_IDS:
        return None
    return id


def generate_get_header_block(url: str):
    return {
        "url": url,
        "accept": 'application/json',
        "content_type": 'application/json',
        "method": 'GET',
        "app_key" : os.getenv("API_APP_KEY"),
        "secret_key": os.getenv("API_APP_SECRET"),
    }

def clean_and_encode_params(params: dict):
    params = {k: v for k, v in params.items() if v is not None}
    params = dict(sorted(params.items()))
    return urlencode(params)

def build_headers_with_hmac (url: str, accept: str, content_type: str, method: int, app_key: str, secret_key: str):
    parsed_url = urlparse(url)

    host = parsed_url.netloc
    path = f"{parsed_url.path}?{parsed_url.query}" if parsed_url.query else parsed_url.path

    # [ToDo] Add MD5 Hashing for Content for POST-Requests
    md5_content: str = ""
    GMT_FORMAT = "%a, %d %b %Y %H:%M:%S GMT"
    x_date = datetime.datetime.utcnow().strftime(GMT_FORMAT)

    signing_str = "x-date: %s\n%s\n%s\n%s\n%s\n%s" % (
        x_date,
        method,
        accept,
        content_type,
        md5_content,
        path,
    )
    hmac_signature = hmac.new(secret_key.encode(), msg=signing_str.encode('utf-8'), digestmod=hashlib.sha1).digest()
    hmac_signature = base64.b64encode(hmac_signature).decode()
    authorization = f"hmac id=\"{app_key}\", algorithm=\"hmac-sha1\", headers=\"x-date\", signature=\"{hmac_signature}\""

    return {"Host": host, "Accept": accept, "Content-Type": content_type, "x-date": x_date, "Authorization": authorization}

def call_api(url: str, app_key: str, secret_key: str):
    url_info = urlparse(url)
    host = url_info.hostname
    path = url_info.path

    if url_info.query:
        query_str = url_info.query
        split_str = query_str.split("&")
        sorted_query = "&".join(sorted(split_str))
        path += "?" + unquote(sorted_query)

    gmt_format = "%a, %d %b %Y %H:%M:%S GMT"
    x_date = datetime.datetime.utcnow().strftime(gmt_format)
    content_md5 = ""
    signing_str = f"x-date: {x_date}\nGET\napplication/json\napplication/json\n{content_md5}\n{path}"

    sign = hmac.new(secret_key.encode(), msg=signing_str.encode(), digestmod=hashlib.sha1).digest()
    signature = base64.b64encode(sign).decode()
    authorization = f'hmac id="{app_key}", algorithm="hmac-sha1", headers="x-date", signature="{signature}"'

    headers = {
        "Host": host,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-date": x_date,
        "Authorization": authorization
    }

    return requests.get(url, headers=headers)