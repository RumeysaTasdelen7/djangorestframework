from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

# urlpatterns = [
#     path("<int:pk>/", views.PostDetail.as_view()),
#     path("", views.PostList.as_view()),
#     path("users/", views.UserList.as_view()),
#     path("users/<int:pk>/", views.UserDetail.as_view()),
# ]

router = SimpleRouter()
router.register("", views.PostViewSet, basename="posts")
router.register("users", views.UserViewSet, basename="users")

urlpatterns = router.urls
