# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime



 # create your views here.
 def signup_view(request);
    #business logic.
    if request.method == 'GET': 
        # display signup form
        today = datetime.now
        return rener(request,'signup.html',{'today':today})
