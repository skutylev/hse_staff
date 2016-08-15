#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
import datetime
from .models import KINDS_OF_EVENTS
import pytz


class CreateEventForm(forms.Form):
    kind = forms.ChoiceField(widget=forms.Select, choices=KINDS_OF_EVENTS)
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(widget=forms.Textarea(), label='Description', max_length=300)
    start_date = forms.DateTimeField(initial=datetime.datetime.now(tz=pytz.timezone('Europe/Moscow')), widget=forms.DateInput(format='%d.%m.%Y %H:%M:%S'),
                                     input_formats=('%d.%m.%Y %H:%M:%S',))
    end_date = forms.DateTimeField(initial=datetime.datetime.now(tz=pytz.timezone('Europe/Moscow')), widget=forms.DateInput(format='%d.%m.%Y %H:%M:%S'),
                                   input_formats=('%d.%m.%Y %H:%M:%S',))
    is_all_day = forms.BooleanField(required=False)


class CancelEventForm(forms.Form):
    ews_id = forms.CharField(label='ews_id', max_length=200)


class GetListEventsForm(forms.Form):
    start_date = forms.DateTimeField(initial=datetime.datetime.now(),
                                     widget=forms.DateInput(format='%d.%m.%Y %H:%M:%S'),
                                     input_formats=('%d.%m.%Y %H:%M:%S',))
    end_date = forms.DateTimeField(initial=datetime.datetime.now(), widget=forms.DateInput(format='%d.%m.%Y %H:%M:%S'),
                                   input_formats=('%d.%m.%Y %H:%M:%S',))