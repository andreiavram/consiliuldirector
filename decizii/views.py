from django.contrib.auth.decorators import login_required
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from decizii.models import Decizie


class DeciziiListView(ListView):
    template_name = "decizii/decizii_list.html"
    queryset = Decizie.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DeciziiListView, self).dispatch(request, *args, **kwargs)


class DecizieDetailView(DetailView):
    template_name = "decizii/decizie_detail.html"
    queryset = Decizie.objects.all()
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DecizieDetailView, self).dispatch(request, *args, **kwargs)
