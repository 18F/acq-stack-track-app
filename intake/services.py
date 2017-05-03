from intake.models import Request

class CreateRequest(object):
    def perform(self):
        request = Request()
        request.save()
        return request
