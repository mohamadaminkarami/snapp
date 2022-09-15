
from django.urls import path
from products import views
urlpatterns = [
    path('scores/', views.ProductScoreCreateAPIView.as_view(),
         name='product_score'),
]
