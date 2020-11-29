from controller import just_hello

routes = {
    "/users/hello": {"method": "GET", "action": just_hello},
}
