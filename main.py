import jwt

def create_token(data, secret):
    token = jwt.encode(data, secret, algorithm='HS256')
    return token


def verify_signature(token):
    try:
        signature_ok = jwt.decode(token, "acelera", algorithms='HS256')
        return signature_ok
    except:
        return({"error": 2})
