from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateEventForm, GetListEventsForm, CancelEventForm
from .models import Event
from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection

# Set up the connection to Exchange
URL = 'https://mail2.hse.ru/EWS/Exchange.asmx'
USERNAME = 'STAFF\\skutylev'
PASSWORD = "CbCmRb88"
connection = ExchangeNTLMAuthConnection(url=URL,
                                        username=USERNAME,
                                        password=PASSWORD)
service = Exchange2010Service(connection)


def create_event(request):
    if request.method == 'POST' and request.user.is_authenticated():
        form = CreateEventForm(request.POST)
        if form.is_valid():

            event = service.calendar().new_event(
                subject=form.cleaned_data.get('title'),
                text_body=form.cleaned_data.get('description'),
                start=form.cleaned_data.get('start_date'),
                end=form.cleaned_data.get('end_date')
            )

            if form.cleaned_data['is_all_day']:
                event.is_all_day = True

            event.create()

            db_event = Event(subject=form.cleaned_data.get('title'),
                             description=form.cleaned_data.get('description'),
                             start_date=form.cleaned_data.get('start_date'),
                             end_date=form.cleaned_data.get('end_date'),
                             kind=form.cleaned_data.get('kind'),
                             user=request.user,
                             ews_id=event.id)

            db_event.save()
            return HttpResponse('Event successfully created.\n Event id is: {}'.format(event.id))
        else:
            form = CreateEventForm()
            return render(request, 'cals/create_event.html', {'form': form})
    else:
        form = CreateEventForm()
        return render(request, 'cals/create_event.html', {'form': form})


def cancel_event(request):
    if request.method == 'POST' and request.user.is_authenticated():
        form = CancelEventForm(request.POST)
        if form.is_valid():
            # Delete from DB
            db_event = Event.objects.filter(ews_id=form.cleaned_data.get('ews_id'))
            db_event.delete()
            # Delete from Cal
            event = service.calendar().get_event(id=form.cleaned_data.get('ews_id'))
            event.cancel()
            return HttpResponse('Event has been canceled')

        else:
            form = CancelEventForm(request.POST)
            return render(request, 'cals/cancel_event.html', {'form': form})
    else:
        form = CancelEventForm(request.POST)
        return render(request, 'cals/cancel_event.html', {'form': form})


def get_list_events(request):
    if request.method == 'POST'and request.user.is_authenticated():
        form = GetListEventsForm(request.POST)
        if form.is_valid():
            events = service.calendar().list_events(
                start=form.cleaned_data.get('start_date'),
                end=form.cleaned_data.get('end_date'),
                details=False
            )
            return render(request, 'cals/list_events.html', {'events': events.events})
        else:
            form = GetListEventsForm()
            return render(request, 'cals/get_events_form.html', {'form': form})
    else:
        form = GetListEventsForm()
        return render(request, 'cals/get_events_form.html', {'form': form})


def get_list_cals(request):
    if request.user.is_authenticated():
        folders = service.folder().find_folder(parent_id='calendar')
        return render(request, 'cals/list_cals.html', {'folders': folders})
    else:
        return HttpResponse('Forbidden')

