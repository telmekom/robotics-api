import base64
import datetime
import hmac
import hashlib
from urllib.request import *
from urllib.parse import urlparse


def build_headers_with_hmac (url: str, accept: str, content_type: str, method: int, app_key: str, secret_key: str):
    parsed_url = urlparse(url)

    host = parsed_url.netloc
    path = parsed_url.path
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
