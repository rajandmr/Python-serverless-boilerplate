from helpers.success_response import success_resp


def just_hello(request):
    my_text = {
        "message": "Hello"
    }
    return success_resp(my_text)
