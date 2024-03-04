from rest_framework import routers

from apps.client.api.v1.views.client import ClientCategoryViewSet

router = routers.SimpleRouter()

router.register('client_categories', ClientCategoryViewSet)

urlpatterns = []
urlpatterns += router.urls
