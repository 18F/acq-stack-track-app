from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from IPython import embed

from intake.services import *

def index(request):
    context = {}
    return render(request, 'intake/index.html', context)

@login_required
def new_request(request):
    return render(request, 'intake/new_request.html', {})

@login_required
def create_request(request):
    if request.method == 'POST':
        request = CreateRequest().perform()
        return redirect('/requests/' + str(request.pk) + '/start')

@login_required
def mp_threshold_question(request, request_id):
    if request.method == "POST":
        mp_threshold = request.POST.get('above_mp_threshold', None)

        redirect_path = {
            'true': '/requests/' + str(request_id) + '/training',
            'false': '/requests/' + str(request_id) + '/under_mp',
            'not_sure': '/requests/' + str(request_id) + '/training',
        }.get(mp_threshold)

        return redirect(redirect_path)
    else:
        context = {
            'request_id': request_id
        }
        return render(request, 'intake/mp_threshold.html', context)

@login_required
def below_mp_threshold_answer(request, request_id):
    context = {
        'request_id': request_id
    }
    return render(request, 'intake/under_mp_message.html', context)

@login_required
def training_question(request, request_id):
    if request.method == 'POST':
        is_training = request.POST.get('training', None)

        redirect_path = {
            'true': '/requests/' + str(request_id) + '/no_training',
            'false': '/requests/' + str(request_id) + '/internal_or_external'
        }.get(is_training)

        return redirect(redirect_path)
    else:
        context = {
            'request_id': request_id
        }
        return render(request, 'intake/training.html', context)

@login_required
def no_training_answer(request, request_id):
    context = {
        'request_id': request_id
    }
    return render(request, 'intake/no_trainings.html', context)

@login_required
def internal_or_external(request, request_id):
    if request.method == 'POST':
        is_internal = request.POST.get('internal_or_external', None)

        redirect_path = {
            'tts': '/requests/' + str(request_id) + '/approval',
            'external': '/requests/' + str(request_id) + '/no_external'
        }.get(is_internal)

        return redirect(redirect_path)
    else:
        context = {
            'request_id': request_id
        }
        return render(request, 'intake/internal_or_external.html', context)

@login_required
def no_external(request, request_id):
    context = {
        'request_id': request_id
    }
    return render(request, 'intake/no_external.html', context)

@login_required
def approval(request, request_id):
    if request.method == 'POST':
        has_approval = request.POST.get('approval', None)

        redirect_path = {
            'true': '/requests/' + str(request_id) + '/contact',
            'false': '/requests/' + str(request_id) + '/no_approval'
        }.get(has_approval)

        return redirect(redirect_path)
    else:
        context = {
            'request_id': request_id
        }
        return render(request, 'intake/approval.html', context)

@login_required
def contact(request, request_id):
    if request.method == 'POST':
        return redirect('/requests/' + str(request_id) + '/urgency')
    else:
        context = {
            'request_id': request_id
        }
        return render(request, 'intake/contact.html', context)

@login_required
def no_approval(request, request_id):
    context = {
        'request_id': request_id
    }
    return render(request, 'intake/no_approval.html', context)

@login_required
def urgency(request, request_id):
    if request.method == 'POST':
        is_urgent = request.POST.get('urgency', None)

        redirect_path = {
            'true': '/requests/' + str(request_id) + '/urgency_description',
            'false': '/requests/' + str(request_id) + '/description'
        }.get(is_urgent)

        return redirect(redirect_path)
    else:
        context = {
            'request_id': request_id
        }
        return render(request, 'intake/urgency.html', context)

@login_required
def urgency_description(request, request_id):
    if request.method == 'POST':
        return redirect('/requests/' + str(request_id) + '/description')
    else:
        context = {
            'request_id': request_id
        }
        return render(request, 'intake/urgency_description.html', context)

@login_required
def description(request, request_id):
    if request.method == 'POST':
        return redirect('/requests/' + str(request_id) + '/submit_request')
    else:
        context = {
            'request_id': request_id
        }
        return render(request, 'intake/description.html', context)

@login_required
def submit_request(request, request_id):
    context = {
        'request_id': request_id
    }
    return render(request, 'intake/submit_request.html', context)
