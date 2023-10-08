from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("user", views.UserViewSet, basename="user")
router.register("profile", views.ProfileViewSet, basename="profile")

urlpatterns = router.urls