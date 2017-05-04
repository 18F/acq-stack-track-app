from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from IPython import embed

def index(request):
    context = {'message': 'randy..............thank you'}
    return render(request, 'intake/index.html', context)

@login_required
def mp_threshold_question(request):
    if request.method == "POST":
        mp_threshold = request.POST.get('above_mp_threshold', None)

        redirect_path = {
            'true': '/training',
            'false': '/under_mp',
            'not_sure': '/training'
        }.get(mp_threshold)

        return redirect(redirect_path)
    else:
        return render(request, 'intake/mp_threshold.html', {})

@login_required
def below_mp_threshold_answer(request):
    return render(request, 'intake/under_mp_message.html', {})

@login_required
def training_question(request):
    if request.method == 'POST':
        is_training = request.POST.get('training', None)

        redirect_path = {
            'true': '/no_training',
            'false': '/internal_or_external'
        }.get(is_training)

        return redirect(redirect_path)
    else:
        return render(request, 'intake/training.html', {})

@login_required
def no_training_answer(request):
    return render(request, 'intake/no_trainings.html', {})

@login_required
def internal_or_external(request):
    if request.method == 'POST':
        is_internal = request.POST.get('internal_or_external', None)

        redirect_path = {
            'tts': '/approval',
            'external': '/no_external'
        }.get(is_internal)

        return redirect(redirect_path)
    else:
        return render(request, 'intake/internal_or_external.html', {})

@login_required
def no_external(request):
    return render(request, 'intake/no_external.html', {})

@login_required
def approval(request):
    if request.method == 'POST':
        has_approval = request.POST.get('approval', None)

        redirect_path = {
            'true': '/contact',
            'false': '/no_approval'
        }.get(has_approval)

        return redirect(redirect_path)
    else:
        return render(request, 'intake/approval.html', {})

@login_required
def contact(request):
    if request.method == 'POST':
        return redirect('/urgency')
    else:
        return render(request, 'intake/contact.html', {})

@login_required
def no_approval(request):
    return render(request, 'intake/no_approval.html', {})

@login_required
def urgency(request):
    if request.method == 'POST':
        is_urgent = request.POST.get('urgency', None)

        redirect_path = {
            'true': '/urgency_description',
            'false': '/description'
        }.get(is_urgent)

        return redirect(redirect_path)
    else:
        return render(request, 'intake/urgency.html', {})

@login_required
def urgency_description(request):
    if request.method == 'POST':
        return redirect('/description')
    else:
        return render(request, 'intake/urgency_description.html', {})

@login_required
def description(request):
    if request.method == 'POST':
        return redirect('/submit_request')
    else:
        return render(request, 'intake/description.html', {})

@login_required
def submit_request(request):
    return render(request, 'intake/submit_request.html', {})

def logout_view(request):
    logout(request)
    return redirect('/')
