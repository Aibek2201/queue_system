from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from . import choices
from .models import Queue


def welcome(request):
    response = render_to_string('queues/welcome.html')
    return HttpResponse(response)


def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Queue, id=ticket_id)
    return render(request, 'queues/ticket_detail.html', {'ticket': ticket})


def queue_list(request):
    # queues = Queue.objects.all()
    queues = Queue.objects.filter(queue_type=choices.QueueTypeChoices.Grant, status=choices.QueueStatusChoices.New)
    return render(request, 'queues/queue_list.html', {'queues': queues})


@csrf_exempt
def queue_create(request):
    queue_type = request.POST.get('queue_type')
    if request.method == 'POST':
        if queue_type == 'Grant':
            queue_type = choices.QueueTypeChoices.Grant
        if queue_type == 'Budget':
            queue_type = choices.QueueTypeChoices.Budget
        if queue_type == 'Other':
            queue_type = choices.QueueTypeChoices.Other
        queue = Queue.objects.create(queue_type=queue_type)
        ticket_id = queue.id
        return redirect('queues:ticket_detail', ticket_id=ticket_id)
    else:
        return render(request, 'queues/queue_create.html', {'queue_type': queue_type})


def queue_monitoring(request):
    queues_in_progress = Queue.objects.filter(status=choices.QueueStatusChoices.ProcessInProgress)

    window_numbers = {
        '1-2': 1,
        '3-4': 2,
        '5-6': 3
    }

    return render(request, 'queues/queue_monitoring.html',
                  {'queues_in_progress': queues_in_progress, 'window_numbers': window_numbers})


def accept(request):
    queue_in_process = Queue.objects.filter(status=choices.QueueStatusChoices.ProcessInProgress).first()
    context = {
        'queue_in_process': queue_in_process
    }
    response = render(request, 'queues/accept.html', context)
    return response


def get_first_queue(request):
    queue_to_end = Queue.objects.filter(queue_type=choices.QueueTypeChoices.Grant,
                                        status=choices.QueueStatusChoices.ProcessInProgress).first()
    queue_to_process = Queue.objects.filter(queue_type=choices.QueueTypeChoices.Grant,
                                            status=choices.QueueStatusChoices.New).first()
    queue_to_end.status = choices.QueueStatusChoices.End
    queue_to_end.save()
    queue_to_process.status = choices.QueueStatusChoices.ProcessInProgress
    queue_to_process.user = request.user.username
    queue_to_process.save()
    return redirect('queues:accept',)

