from django.conf import settings
from django.urls import path, include
from django.views.generic.base import TemplateView

from feedback import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="feedback/main.html"), name='feedback_main'),
    path('list', views.FeedbackList.as_view(), name='feedback_list'),
    path('create', views.FeedbackCreate.as_view(), name='feedback_create'),
    path('update/<int:pk>', views.FeedbackUpdate.as_view(), name='feedback_update'),
    path('delete/<int:pk>', views.FeedbackDelete.as_view(), name='feedback_delete'),
    path('<int:pk>', views.FeedbackDetail.as_view(), name='feedback_detail'),
]

# if settings.DEBUG:
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#     urlpatterns += staticfiles_urlpatterns()