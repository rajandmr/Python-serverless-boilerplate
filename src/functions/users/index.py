import json
import traceback
from routes import routes
from helpers.error_response import error_resp


def main(event, context):
    path = event['path']
    try:
        action = routes[path]["action"]
        print(path)
        body = event['body']
        if body is None:
            body = "{}"
        response = action(request=json.loads(body))

    except Exception:
        print(traceback.format_exc())
        response = error_resp({"message": traceback.format_exc()})

    return response


if __name__ == "__main__":
    main(None, None)
