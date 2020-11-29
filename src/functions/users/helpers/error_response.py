import json


def error_resp(body):
    response = {
        "statusCode": 500,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "text/plain",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        }
    }

    return response
