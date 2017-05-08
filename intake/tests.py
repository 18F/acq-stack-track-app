from django.test import TestCase, RequestFactory

from intake.models import Request
from intake.services import CreateRequest, UpdateRequest, UpdateRequestException

# mock login_required before we import the views that have been decorated by it
# more info: http://alexmarandon.com/articles/python_mock_gotchas/#patching-decorators
from unittest.mock import Mock, patch
patch('django.contrib.auth.decorators.login_required', lambda x: x).start()
import intake.views as views

from datetime import datetime

from IPython import embed

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

    def test_init_with_unpermitted_param(self):
        request_model = Request()
        request_model.save()
        with self.assertRaises(UpdateRequestException):
            update_request = UpdateRequest(request_model.pk, {'banned_param':True})

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

    def test_below_mp_threshold_answer(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.below_mp_threshold_answer(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_training_question_get_request(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.training_question(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_training_question_post_request(self):
        # test is training
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'is_training': 'true'
        }
        request = request_factory.post('', post_data)
        response = views.training_question(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.is_training, True)
        self.assertEqual(response.status_code, 302)

        # test is not training
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'is_training': 'false'
        }
        request = request_factory.post('', post_data)
        response = views.training_question(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.is_training, False)
        self.assertEqual(response.status_code, 302)

    def test_no_training_answer(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.no_training_answer(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_internal_or_external_get_request(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.internal_or_external(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_internal_or_external_post_request(self):
        # test is internal
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'is_internal': 'true'
        }
        request = request_factory.post('', post_data)
        response = views.internal_or_external(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.is_internal, True)
        self.assertEqual(response.status_code, 302)

        # test is not internal
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'is_internal': 'false'
        }
        request = request_factory.post('', post_data)
        response = views.internal_or_external(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.is_internal, False)
        self.assertEqual(response.status_code, 302)

    def test_no_external(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.no_external(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_approval_get_request(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.approval(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_approval_post_request(self):
        # client lacks approval
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'client_has_approval': 'false'
        }
        request = request_factory.post('', post_data)
        response = views.approval(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.client_has_approval, False)
        self.assertEqual(response.status_code, 302)

        # client has approval
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'client_has_approval': 'true'
        }
        request = request_factory.post('', post_data)
        response = views.approval(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.client_has_approval, True)
        self.assertEqual(response.status_code, 302)

    def test_contact_get_request(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.contact(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_contact_post_request(self):
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'client_contact': '@adelevie on slack'
        }
        request = request_factory.post('', post_data)
        response = views.contact(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.client_contact, '@adelevie on slack')
        self.assertEqual(response.status_code, 302)

        # client leaves contact blank
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'client_contact': ''
        }
        request = request_factory.post('', post_data)
        response = views.contact(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.client_contact, '')
        self.assertEqual(response.status_code, 302)

    def test_no_approval_get_request(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.no_approval(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_urgency_get_request(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.urgency(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_urgency_post_request(self):
        request_factory = RequestFactory()
        post_data = {
            'urgency': 'true'
        }
        request = request_factory.post('', post_data)
        response = views.urgency(request, 12)
        self.assertEqual(response.status_code, 302)

        request_factory = RequestFactory()
        post_data = {
            'urgency': 'false'
        }
        request = request_factory.post('', post_data)
        response = views.urgency(request, 12)
        self.assertEqual(response.status_code, 302)

    def test_urgency_description_get_request(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.urgency_description(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_urgency_description_post_request(self):
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'urgency': 'this is very urgent'
        }
        request = request_factory.post('', post_data)
        response = views.urgency_description(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.urgency, 'this is very urgent')
        self.assertEqual(response.status_code, 302)

    def test_description_get_request(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.description(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_description_post_request(self):
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'description': 'I want to buy some widgets'
        }
        request = request_factory.post('', post_data)
        response = views.description(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.description, 'I want to buy some widgets')
        self.assertEqual(response.status_code, 302)

    def test_submit_request_get_request(self):
        request_factory = RequestFactory()
        request = request_factory.get('')
        response = views.submit_request(request, 12)
        self.assertEqual(response.status_code, 200)

    def test_submit_request_post_request(self):
        request_model = Request()
        request_model.save()
        request_factory = RequestFactory()
        post_data = {
            'submit': 'true'
        }
        request = request_factory.post('', post_data)
        response = views.submit_request(request, request_model.pk)
        request_model.refresh_from_db()
        self.assertEqual(request_model.submitted_at.__class__, datetime)
