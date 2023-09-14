from django.utils.crypto import get_random_string


class CreateSessionKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the session key is not set, generate a new one and save it
        if not request.session.session_key:
            session_key = get_random_string(32)
            request.session.create()
            request.session["session_key"] = session_key
            request.session.modified = True

        response = self.get_response(request)

        return response
