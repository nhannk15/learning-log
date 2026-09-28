from django.urls import path
from . import views

app_name = "learning_logs"

urlpatterns = [
    path('', views.hello, name="index"),
    path('about/', views.about, name="about"),
    path('topics/', views.topics, name="topics"),
    path('topics/<int:topic_id>/', views.topic, name="topic")
]