from django.test import TestCase, RequestFactory

from intake.models import Request
from intake.services import CreateRequest, UpdateRequest

# mock login_required before we import the views that have been decorated by it
# more info: http://alexmarandon.com/articles/python_mock_gotchas/#patching-decorators
from unittest.mock import Mock, patch
patch('django.contrib.auth.decorators.login_required', lambda x: x).start()
import intake.views as views

class CreateRequestTestCase(TestCase):
    def test_perform_with_no_args(self):
        create_request = CreateRequest()
        self.assertEqual(Request.objects.count(), 0)
        request = create_request.perform()
        self.assertEqual(Request.objects.count(), 1)
        self.assertEqual(type(request.pk), int)

class UpdateRequestTestCase(TestCase):
    def test_perform_with_args(self):
        request_model = Request()
        request_model.save()
        update_request = UpdateRequest(request_model.pk, {'below_mp_threshold':True})
        update_request.perform()
        request_model.refresh_from_db()
        self.assertEqual(request_model.below_mp_threshold, True)

class IntakeViewsTestCase(TestCase):
    def test_create_request(self):
        self.assertEqual(Request.objects.count(), 0)

        request_factory = RequestFactory()
        request = request_factory.post('')
        response = views.create_request(request)

        # check that request record was saved
        self.assertEqual(Request.objects.count(), 1)

        request_that_was_just_created = Request.objects.all()[0]

        # check that the response redircts to the proper url
        self.assertEqual(response.url, '/requests/' + str(request_that_was_just_created.pk) + '/start')
        self.assertEqual(response.status_code, 302)

    def test_mp_threshold_question_get_request(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.mp_threshold_question(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_mp_threshold_question_post_request(self):
        # test below mp threshold
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'below_mp_threshold': 'true'
        }
        request = request_factory.post('', post_data)
        response = views.mp_threshold_question(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.below_mp_threshold, True)
        self.assertEqual(response.status_code, 302)

        # test above mp threshold
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'below_mp_threshold': 'false'
        }
        request = request_factory.post('', post_data)
        response = views.mp_threshold_question(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.below_mp_threshold, False)
        self.assertEqual(response.status_code, 302)

        # test "not sure" mp threshold
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'below_mp_threshold': 'none'
        }
        request = request_factory.post('', post_data)
        response = views.mp_threshold_question(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.below_mp_threshold, None)
        self.assertEqual(response.status_code, 302)
