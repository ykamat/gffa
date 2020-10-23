
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User
from apps.webapp.models import Person

from .serializers import PersonSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        queryset = Person.objects.all()
        name = self.request.query_params.get('search', None)
        if name is not None:
            queryset = queryset.filter(name__contains=name)
        return queryset.order_by('person_id')

