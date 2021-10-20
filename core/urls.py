from django.urls import path, include
from .views import Home, BucketHome, BucketDelete, BucketDownolad, BucketUpload
from .api_views import (
    QuestionListView, QuestionCreateView,
    QuestionUpdateView, QuestionDeleteView,
    AnswerCreateView,AnswerUpdateView,
    AnswerDeleteView,
)


app_name='core'

api_urls = [
    path('questions/', QuestionListView.as_view()),
    path('questions/create/', QuestionCreateView.as_view()),
    path('questions/update/<int:pk>/', QuestionUpdateView.as_view()),
    path('questions/delete/<int:pk>/', QuestionDeleteView.as_view()),
    path('answers/create/', AnswerCreateView.as_view()),
    path('answers/update/<int:pk>/', AnswerUpdateView.as_view()),
    path('answers/delete/<int:pk>/', AnswerDeleteView.as_view()),
]

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('bucket/', BucketHome.as_view(), name='bucket_home'),
    path('bucket_delete/<str:key>/', BucketDelete.as_view(), name='bucket_delete'),
    path('bucket_download/<str:key>/', BucketDownolad.as_view(), name='bucket_download'),
    path('bucket_upload/', BucketUpload.as_view(), name='bucket_upload'),
    path('api/', include(api_urls)),
]