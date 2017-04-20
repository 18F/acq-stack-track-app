class FakeRequest(object):
    def __init__(self):
        self.pk = 12

class CreateRequest(object):
    def perform(self):
        return FakeRequest()

class FindRequest(object):
    def __init__(self, pk):
        self._pk = pk

    def perform(self):
        return FakeRequest()
