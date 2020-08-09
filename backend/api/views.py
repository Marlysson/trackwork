from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


