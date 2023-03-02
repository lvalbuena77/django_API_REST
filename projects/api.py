from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Esto es para que se vean todos los proyectos.
    permission_classes = [permissions.AllowAny] # Esto es para que cualquiera pueda ver los proyectos, pero no modificarlos.
    serializer_class = ProjectSerializer
    