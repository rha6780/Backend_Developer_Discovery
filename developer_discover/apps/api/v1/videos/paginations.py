from rest_framework.pagination import PageNumberPagination


class VideoListPagination(PageNumberPagination):
    page_size = 4
