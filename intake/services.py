from intake.models import Request

class CreateRequest(object):
    def perform(self):
        request = Request()
        request.save()
        return request

class UpdateRequest(object):
    def __init__(self, request_id, attributes):
        self._request_id = request_id
        self._attributes = attributes

    def perform(self):
        return Request.objects.filter(pk=self._request_id).update(**self._attributes)
