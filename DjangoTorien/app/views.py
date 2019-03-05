"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import app.models as M

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #categories = M.Category.objects.all()[:9]
    th = M.Thing.objects.all().order_by('-date_add')
    th.query.group_by = ['collection']
    categories = th[:9]
    collections = M.Collection.objects.all().order_by('-data_create')[:2]
    ret = {}
    ret['collections'] = collections
    ret['categories'] = categories
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'res': ret,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
