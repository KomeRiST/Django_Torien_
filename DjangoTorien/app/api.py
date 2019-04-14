from django.http import HttpResponse
import json
from django.core import serializers # Для сериализации обьектов
from django.db.models import Count, Min, Sum, Avg, Subquery, OuterRef, F
import app.models as M

def APIgetcategory(request):
    """Renders the contact page."""
    #assert isinstance(request, HttpRequest)
    if request.method == "GET":
        s = request.GET["size"]
        if s == '-1':
            th = M.Relationship.objects.all()
        else:
            th = M.Relationship.objects.filter(size=s)
        th = th.values('thing__category__id').\
            annotate(\
                name = F('thing__category__name'),\
                thing_count=Sum('count'), \
                thing_cost_min=Min('thing__cost'), \
                ).\
            values('thing__category__id', 'name', 'thing_count', 'thing_cost_min')
        res = list(th)
        return HttpResponse(json.dumps(res), content_type = "application/json")
        #date = serialize('json', th)
        #return JsonResponse(date)

def APIgetthings(request):
    """Renders the contact page."""
    #assert isinstance(request, HttpRequest)
    if request.method == "GET":
        s = request.GET["size"]
        c = request.GET["category"]
        if s == '-1':
            r = M.Relationship.objects.all()
        else:
            r = M.Relationship.objects.filter(size=s)
        if c != '-1':
            th = r.values('thing').filter(thing__category_id=c).annotate(id=F('thing__id'), name=F('thing__name'), cost=F('thing__cost'), image=Min('thing__images__image')).values('id', 'name', 'cost', 'image')
            print(th.query)
        else:
            th = k.values('thing').annotate(id=F('thing__id'), name=F('thing__name'), cost=F('thing__cost'), image=Min('thing__images__image')).values('id', 'name', 'cost', 'image')
            print(th.query)
        res = list(th)
        return HttpResponse(json.dumps(res), content_type = "application/json")