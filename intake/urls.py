from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start', views.mp_threshold_question, name='mp_threshold_question'),
    url(r'^under_mp', views.below_mp_threshold_answer, name='below_mp_threshold_answer'),
    url(r'^training', views.training_question, name='training_question'),
    url(r'^no_training', views.no_training_answer, name='no_training_answer'),
    url(r'^internal_or_external', views.internal_or_external, name='internal_or_external'),
    url(r'^no_external', views.no_external, name='no_external'),
    url(r'^approval', views.approval, name='approval'),
    url(r'^no_approval', views.no_approval, name='no_approval'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^urgency_description', views.urgency_description, name='urgency_description'),
    url(r'^urgency', views.urgency, name='urgency'),
    url(r'^description', views.description, name='description'),
    url(r'^submit_request', views.submit_request, name='submit_request')
]
