from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start', views.mp_threshold_question, name='mp_threshold_question'),
    url(r'^under_mp', views.below_mp_threshold_answer, name='below_mp_threshold_answer'),
    url(r'^training', views.training_question, name='training_question'),
    url(r'^no_training', views.no_training_answer, name='no_training_answer'),
    url(r'^internal_or_external', views.internal_or_external, name='internal_or_external')
]
