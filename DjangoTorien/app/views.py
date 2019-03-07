"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.db.models import Count, Min, Sum, Avg
from datetime import datetime
import app.models as M

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    th = M.Relationship.objects.filter(thing__category_id__gte=0).values('thing__category', 'thing__category__name', 'thing__category__icon').annotate(thing_count=Sum('count'), thing_cost_min=Min('thing__cost'), thing_cost_avg=Avg('thing__cost')).order_by('-thing__date_add')[:9]
    print(th.query)
    print(th[0])
    print(th[1])
    collections = M.Collection.objects.all().order_by('-data_create')[:2]
    ret = {}
    ret['collections'] = collections
    ret['categories'] = th
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
