from rest_framework import routers

from posts import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = router.urls
