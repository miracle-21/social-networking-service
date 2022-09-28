from django.urls import path

from users.views import UserViewSet

urlpatterns = [
    path('', UserViewSet.as_view(actions={'get': 'list'})),
    path('<int:pk>/', UserViewSet.as_view(actions={'patch': 'partial_update', 'delete': 'destroy'})),
    path('signup/', UserViewSet.as_view(actions={'post': 'create'})),
]