from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)


class LimitOffsetPagination(LimitOffsetPagination):
    default_limit = 50 # Num of Items on a Page
    max_limit = 50 