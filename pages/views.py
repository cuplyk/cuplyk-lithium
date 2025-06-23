from django.views.generic import TemplateView
from visits.views import PageVisitsView
from visits.models import PageVisits



class HomePageView(PageVisitsView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
