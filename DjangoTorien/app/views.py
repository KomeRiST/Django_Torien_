"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.db.models import Count, Min, Sum, Avg, Subquery, OuterRef, F
from datetime import datetime
import app.models as M

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #th = M.Thing.random_image(OuterRef('thing'))
    #subquery = M.Gallery.objects.filter(thing=OuterRef('thing')).order_by('?').values('image')[:1]

    #th = M.Relationship.objects.\
    #    all().\
    #    values('thing__category__id').\
    #    annotate(\
    #        name = F('thing__category__name'),\
    #        thing_count=Sum('count'), \
    #        thing_cost_min=Min('thing__cost'), \
    #        thing_cost_avg=Avg('thing__cost'), \
    #        thing_img=F('thing__random_image')
    #        ).\
    #        order_by('-thing__date_add').\
    #        values('name', 'thing_count', 'thing_cost_min', 'thing_cost_avg', 'thing_img')
    #print(th.query)
    #print(th[0])
    #print(th[1])
    th = M.Relationship.objects.raw('SELECT app_relationship."id", app_category."name" AS name,\
       SUM(app_relationship."count") AS thing_count,\
       MIN(app_thing."cost") AS thing_cost_min,\
       AVG(app_thing."cost") AS thing_cost_avg,\
       (\
           SELECT U0.image\
             FROM app_gallery U0\
            WHERE U0.thing_id = (app_relationship."thing_id") \
            ORDER BY RANDOM() ASC\
            LIMIT 1\
       )\
       AS thing_img\
  FROM app_relationship\
       INNER JOIN\
       app_thing ON (app_relationship."thing_id" = app_thing."id") \
       INNER JOIN\
       app_category ON (app_thing."category_id" = app_category."id") \
 GROUP BY app_thing."category_id"\
 ORDER BY app_thing."date_add" DESC;')
    collections = M.Collection.objects.all().order_by('-data_create')[:1]
    ret = {}
    ret['collection'] = collections
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

def collection(request, _id):
    assert isinstance(request, HttpRequest)
    res = {}
    res["collection"] = M.Collection.objects.get(id=_id)
    return render(
        request,
        'app/collection.html',
        {
            'res': res,
            'title':'Коллекции',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def collections(request):
    assert isinstance(request, HttpRequest)
    res = {}
    res["collections"] = M.Collection.objects.all().order_by("-data_create")
    return render(
        request,
        'app/collections.html',
        {
            'res': res,
            'title':'Коллекции',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def collections2(request):
    assert isinstance(request, HttpRequest)
    res = {}
    res["collections"] = M.Collection.objects.all().order_by("-data_create")
    return render(
        request,
        'app/collections2.html',
        {
            'res': res,
            'title':'Коллекции',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
