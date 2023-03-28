from rest_framework import routers
from core.usermanagement.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet

router = routers.SimpleRouter()



router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='register')
router.register(r'auth/login', LoginViewSet, basename='login')
router.register(r'auth/refresh', RefreshViewSet, basename='refresh')

urlpatterns =[
    *router.urls
]