

from django.conf import settings
from django.views.generic import TemplateView


class IndexView(TemplateView):

    tempate_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super(IndexView).get_context_data(**kwargs)
        context['site_name'] = settings.SITE_NAME
        return context
