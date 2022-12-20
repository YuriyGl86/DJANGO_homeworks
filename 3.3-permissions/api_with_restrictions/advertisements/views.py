from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwnerOrAdminOrReadOnly
from .filters import AdvertisementFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AdvertisementFilter
    serializer_class = AdvertisementSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdminOrReadOnly()]
        return []

    @action(methods=['post', 'get'], detail=True)
    def favorites(self, request, pk=None):
        if self.request.method == "GET":
            print(request.user)
            # favorite_list = Advertisement.objects.filter(favorites__username=request.user)
            favorite_list = Advertisement.objects.filter(favorites=request.user)
            return Response({'favorites': [c.id for c in favorite_list]})

        elif request.user.id != Advertisement.objects.get(pk=pk).creator.id:
            request.user.advertisements.add(Advertisement.objects.get(pk=pk))
            return Response({'Favorites': 'success'})
        else:
            return Response({'Favorites: Failed. Вы не можете добавить в избранное свое же объявление'})

    def get_queryset(self):
        queryset = Advertisement.objects.exclude(Q(status='DRAFT') & ~Q(creator=self.request.user.id))
        return queryset
