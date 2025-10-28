from django.views.generic import TemplateView
<<<<<<< HEAD
from visits.views import PageVisitsView
from visits.models import PageVisits



class HomePageView(PageVisitsView):
=======


class HomePageView(TemplateView):
>>>>>>> 67e56f3 (initial commit)
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
