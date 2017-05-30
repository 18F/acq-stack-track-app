from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^requests/new', views.new_request, name='new_request'),
    url(r'^requests/create', views.create_request, name='create_request'),
    url(r'^requests/all', views.big_board, name='big_board'),
    url(r'^requests/(?P<request_id>\d+)/start', views.mp_threshold_question, name='mp_threshold_question'),
    url(r'^requests/(?P<request_id>\d+)/under_mp', views.below_mp_threshold_answer, name='below_mp_threshold_answer'),
    url(r'^requests/(?P<request_id>\d+)/training', views.training_question, name='training_question'),
    url(r'^requests/(?P<request_id>\d+)/no_training', views.no_training_answer, name='no_training_answer'),
    url(r'^requests/(?P<request_id>\d+)/internal_or_external', views.internal_or_external, name='internal_or_external'),
    url(r'^requests/(?P<request_id>\d+)/no_external', views.no_external, name='no_external'),
    url(r'^requests/(?P<request_id>\d+)/approval', views.approval, name='approval'),
    url(r'^requests/(?P<request_id>\d+)/no_approval', views.no_approval, name='no_approval'),
    url(r'^requests/(?P<request_id>\d+)/contact', views.contact, name='contact'),
    url(r'^requests/(?P<request_id>\d+)/urgency_description', views.urgency_description, name='urgency_description'),
    url(r'^requests/(?P<request_id>\d+)/urgency', views.urgency, name='urgency'),
    url(r'^requests/(?P<request_id>\d+)/description', views.description, name='description'),
    url(r'^requests/(?P<request_id>\d+)/submit_request', views.submit_request, name='submit_request'),
    url(r'^requests/(?P<request_id>\d+)/submitted', views.request_submitted, name='request_submitted'),
]
