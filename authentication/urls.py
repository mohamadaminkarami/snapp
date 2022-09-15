
from django.urls import path, include
from authentication import views
urlpatterns = [
    path('register/', views.RegisterCreateAPIView.as_view(), name='register'),
    path('', include('rest_framework.urls'))
]
