from django.shortcuts import redirect, render
from IPython import embed

def index(request):
    context = {'message': 'randy..............thank you'}
    return render(request, 'intake/index.html', context)

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

def below_mp_threshold_answer(request):
    return render(request, 'intake/under_mp_message.html', {})

def training_question(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'intake/training.html', {})
