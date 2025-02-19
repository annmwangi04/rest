from django.urls import path
from .views import CourseView

urlpatterns = [
    path('', CourseView.as_view(), name='course.view'),
    path('<int:id>',CourseView.as_view(), name='course.view')
]
