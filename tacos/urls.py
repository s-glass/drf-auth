from django.urls import path
from .views import TacoList, TacoDetail

urlpatterns = [
    path('', TacoList.as_view(), name='taco_list'),
    path('<int:pk>', TacoDetail.as_view(), name='taco-detail'),
]