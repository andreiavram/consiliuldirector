from django.contrib.auth.decorators import login_required
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from decizii.models import Decizie


class DeciziiListView(ListView):
    template_name = "decizii/decizii_list.html"
    queryset = Decizie.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DeciziiListView, self).dispatch(request, *args, **kwargs)

