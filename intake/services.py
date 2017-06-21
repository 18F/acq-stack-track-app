from intake.models import Request

from IPython import embed

class CreateRequest(object):
    def __init__(self, **kwargs):
        self._user_id = kwargs.get('user_id')
        if self._user_id is None:
            raise Exception('user_id is missing')

    def perform(self):
        request = Request(user_id=self._user_id)
        request.save()
        return request

class UpdateRequest(object):
    def __init__(self, request_id, attributes):
        self._request_id = request_id
        self._attributes = {}

        attributes_copy = attributes.copy()

        if attributes_copy.get('csrfmiddlewaretoken'):
            attributes_copy.pop('csrfmiddlewaretoken')

        for key, _ in attributes_copy.items():
            if key not in self._permitted_params():
                raise UpdateRequestException("Attribute {} not permitted.".format(key))

        for param in self._permitted_params():
            if attributes.get(param) is not None:
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
