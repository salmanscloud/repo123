from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'classes', ClassViewSet, basename='class')
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('students/', include(router.urls)), #API endpoint for adding students
    path('students/<int:pk>/', include(router.urls)), #API endpoint for deleting students
    path('classes/', include(router.urls)), #API endpoint for listing class
    path('classes/<int:pk>/', include(router.urls)), #API endpoint for details of clsss
    

]