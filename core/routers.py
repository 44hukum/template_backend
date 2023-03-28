from rest_framework import routers
from core.usermanagement.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet

router = routers.SimpleRouter()



router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='register')

urlpatterns =[
    *router.urls
]