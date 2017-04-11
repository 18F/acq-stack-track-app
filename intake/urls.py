from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start', views.mp_threshold_question, name='mp_threshold_question'),
    url(r'^under_mp', views.below_mp_threshold_answer, name='below_mp_threshold_answer'),
    url(r'^training', views.training_question, name='training_question'),
]
