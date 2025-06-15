from django.shortcuts import render
from .models import PageVisits
from django.views.generic import TemplateView
# Create your views here.
class PageVisitsView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get visit statistics
        total_visits = PageVisits.objects.all()
        current_page_visits = PageVisits.objects.filter(path=self.request.path)
        
        # Calculate percentage
        total_count = total_visits.count()
        page_count = current_page_visits.count()
        
        if total_count > 0:
            percentage = round((page_count * 100.0) / total_count, 1)
        else:
            percentage = 0
        
        # Add data to template context
        context.update({
            "page_title": "Home",
            "page_visit_count": page_count,
            "percent": percentage,
            "total_visit_count": total_count,
        })
        
        # Record this visit
        PageVisits.objects.create(path=self.request.path)
        
        return context
