from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from course.models import Course
from course.serializers import CourseDetailSerializer, CourseListSerializer


class CourseCreateView(generics.CreateAPIView):
    serializer_class = CourseDetailSerializer


class CourseListView(generics.ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('start_date', 'end_date')


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
