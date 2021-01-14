from controller import just_hello, create_user, get_all, get_one, delete_user, edit_user


routes = {
    "/users/hello": {"method": "GET", "action": just_hello},
    "/users/create": {"method": "POST", "action": create_user},
    "/users/getall": {"method": "GET", "action": get_all},
    "/users/getone": {"method": "GET", "action": get_one},
    "/users/delete": {"method": "DELETE", "action": delete_user},
    "/users/edit": {"method": "PUT", "action": edit_user},
}
