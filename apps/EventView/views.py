from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from Common.GetData.getEvent import get_event


@login_required
def list_event(request):
    events = get_event()
    context = {
        "user_": "Hiencoday",
        'events': events
    }
    return render(request, 'home/home.html', context)
