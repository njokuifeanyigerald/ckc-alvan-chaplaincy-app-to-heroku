from django.shortcuts import render,get_object_or_404
from api.models import Marriage,Baptism,Reading,Annoucement
from django.views.generic import ListView, TemplateView
from django.db.models import Q

class HomeView(TemplateView):
    template_name = "home.html"
def choir_view(request):
    return render(request,'choir.html',{})
def altar_view(request):
    return render(request, 'altar servers.html', {})
def cwo_view(request):
    return render(request,'cwo.html',{})
def cmo_view(request):
    return render(request,'cmo.html',{})
def block_rosary_view(request):
    return render(request,'block rosary.html',{})
def marrige_list_view(request):
    queryset = Marriage.objects.order_by('-date_of_marriage')
    context = {
        "form":queryset
    }
    return render(request, 'marriage.html', context)
class MarriageSearchView(ListView):
    model = Marriage
    template_name = "marriage_search.html"
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Marriage.objects.filter(
            Q(name_of_groom__icontains=query)|Q(name_of_bride__icontains=query)
        )
        return object_list

def baptism_list_view(request):
    queryset = Baptism.objects.order_by('-date_of_baptism')
    context = {
        "form":queryset
    }
    return render(request, 'baptism.html', context)

def baptism_detail_view(request, id):
    queryset = get_object_or_404(Baptism, id=id)
    context = {
        "form":queryset
    }
    return render(request, 'baptism_details.html', context)

class BaptismSearchView(ListView):
    model = Baptism
    template_name = 'baptism_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Baptism.objects.filter(
            Q(baptismal_name__icontains=query)|Q(name__icontains=query)
        )
def marriage_detail_view(request, id):
    queryset = get_object_or_404(Marriage,id=id)
    context = {
        "form":queryset
    }
    return render(request, 'marriage_details.html', context)

def readings_view(request):
    queryset = Reading.objects.order_by('-date')
    context = {
        "form": queryset
    }
    return render(request,'readings.html', context)
def announcement_view(request):
    queryset = Annoucement.objects.order_by('-date')
    context = {
        "form": queryset
    }
    return render(request,'announcement.html', context)
def readings_detail_view(request, id):
    queryset = get_object_or_404(Reading,id=id)
    context = {
        "form":queryset
    }
    return render(request, 'reading_details.html', context)
def announcement_detail_view(request, id):
    queryset = get_object_or_404(Annoucement,id=id)
    context = {
        "form":queryset
    }
    return render(request, 'announcement_details.html', context)