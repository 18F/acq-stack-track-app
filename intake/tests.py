from django.test import TestCase

from intake.models import Request
from intake.services import CreateRequest

class CreateRequestTestCase(TestCase):
    def test_perform_with_no_args(self):
        create_request = CreateRequest()
        self.assertEqual(Request.objects.count(), 0)
        request = create_request.perform()
        self.assertEqual(Request.objects.count(), 1)
        self.assertEqual(type(request.pk), int)
