from django.urls import path

from . import views


app_name = "polls"
urlpatterns = [
    #ex: /polls
    path("/",views.IndexView.as_view(), name="index"),
    #ex/polls/5
    path("/<int:pk>/",views.ModelDetailView.as_view(), name="detail"),
    # ex/polls/5/results
    path("/<int:pk>/results/", views.ModelDetailView_Results.as_view(), name="results"),
    path("/<int:question_id>/votes/", views.vote, name="vote"),
]