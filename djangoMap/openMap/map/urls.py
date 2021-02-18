from django.urls import path, include
from rest_framework import routers
from map import views


router = routers.DefaultRouter()

router.register('my_city', views.CityView)
router.register('my_latlong', views.LatLongView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', views.viewmap, name="viewMap"),
    path('search', views.search_map, name="search_map2"),
    path('fromzip', views.data_from_zip),
    path('showpolygon',views.showpolygon),
    path('showsubmap',views.sub_search),
    path('searchmymap',views.search_mymap),
    path('showgis',views.showgis),
    path('showgis2',views.arcgisdemo),
]