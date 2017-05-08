from intake.models import Request

class CreateRequest(object):
    def perform(self):
        request = Request()
        request.save()
        return request

class UpdateRequest(object):
    def __init__(self, request_id, attributes):
        self._request_id = request_id
        self._attributes = {}

        for key, _ in attributes.items():
            if key not in self._permitted_params():
                raise UpdateRequestException("Attribute {} not permitted.".format(key))

        for param in self._permitted_params():
            self._attributes[param] = attributes.get(param)

        for key, value in self._attributes.items():
            if value == 'true':
                self._attributes[key] = True
            if value == 'false':
                self._attributes[key] = False
            if value == 'none':
                self._attributes[key] = None

    def perform(self):
        return Request.objects.filter(pk=self._request_id) \
                              .update(**self._attributes)

    def _permitted_params(self):
        return [
            'below_mp_threshold',
            'is_training',
            'is_internal',
            'client_has_approval',
            'client_contact',
            'urgency',
            'description',
            'submitted_at'
        ]

class UpdateRequestException(Exception):
    pass
