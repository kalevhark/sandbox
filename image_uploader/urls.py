from django.urls import path

from .views import UploadURLView, UploadDetailView

urlpatterns = [
    path('', UploadURLView.as_view(), name="upload-url"),
    path('show/<int:pk>/', UploadDetailView.as_view(), name="upload-detail")
]