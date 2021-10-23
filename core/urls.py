from django.urls import path

from core.views import FeedbackSubmission
from .views import (
#HomeView,
AssignmentCreateView,
AssignmentView,
AssignmentDeleteView,
AssignmentSubmissionView,
AssignmentSubmissionListView,
AssignmentSubmissionDelete
)

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

app_name = "core"

urlpatterns = [
                  path('', TemplateView.as_view(template_name='home.html'), name='home'),
                  path('assignment-create/', AssignmentCreateView.as_view(), name='assignment-create'),
                  path('assignment/', AssignmentView.as_view(), name='assignment-list'),
                  path('<pk>/delete/', AssignmentDeleteView.as_view(), name='delete-assignment'),
                  path('assignment-submission/', AssignmentSubmissionView.as_view(), name='assignment-submission'),
                  path('assignment-submission-list/', AssignmentSubmissionListView.as_view(), name='assignment-submission-list'),
                  path('<pk>/delete/', AssignmentSubmissionDelete.as_view(), name='assignment-submission-delete'),
                  path('assignment/feedback/',FeedbackSubmission.as_view(),name='assignment-feedback'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)