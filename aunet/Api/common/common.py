errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },

    'ResourceDoesNotFound': {
        'message': "A resource with that ID don't exists.",
        'status': 404,
        'extra': "you can try another ID",
    }
}