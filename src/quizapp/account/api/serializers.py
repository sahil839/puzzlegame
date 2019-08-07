from rest_framework.routers import DefaultRouter
from account.api.views import UserViewSet
from .views import AuthenticationCheckAPIView
from django.urls import path

app_name = 'account'

router = DefaultRouter()
router.register(r'user', UserViewSet, base_name='user')

urlpatterns = router.urls + [path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check')]