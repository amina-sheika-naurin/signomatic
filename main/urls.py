
from django.urls import path
from . import views
from .views import SignUpView



urlpatterns = [
    path('', views.index),
    path('home',views.home),
    path('create',views.create),
    path('train',views.train),
    path('predict',views.predict),
    path('signup/', SignUpView.as_view(), name="signup"),
]
