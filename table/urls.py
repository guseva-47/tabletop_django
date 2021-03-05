from rest_framework import routers
from .views import TabletopViewSet, subscribe, UsrViewSet

router = routers.DefaultRouter()
router.register('', TabletopViewSet)
urlpatterns = router.urls

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

suf_paths = [
    path('<int:pk>/sub', subscribe),
]

urlpatterns += format_suffix_patterns(suf_paths)