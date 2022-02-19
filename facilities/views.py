from django.shortcuts import render
# from django_auto_prefetching import AutoPrefetchViewSetMixin
from rest_framework import viewsets

from .models import HealthFacilities, Description, Location
from .serializers import HealthFacilitiesSerializer

from .pagination import LimitOffsetPagination
from rest_framework import status


class FacilitiesViewSet(viewsets.ModelViewSet):

    serializer_class = HealthFacilitiesSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        
        queryset = HealthFacilities.objects.prefetch_related('loc', 'desc')
        shortDescription = self.request.query_params.get('shortDescription', None)
        description = self.request.query_params.get('description', None)
        if shortDescription is not None:
            queryset = queryset.filter(desc__shortDescription=shortDescription)
            return queryset  # cant filter on two different Descriptions so return w/o checking description
        if description is not None:
            queryset = queryset.filter(desc__description=description)        
        return queryset


    # override function to determine if there are too many database hits.
    # Currently using prefetch_related method we are able to keep it under 3 or 4 query 
    # hits per method call. This is usually an issue with nested serializer
    # so need to confirm that it is working properly.
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)

        from django.db import connection
        print('*************** # of Queries: {}   *****************'.format(len(connection.queries)))

        return response
