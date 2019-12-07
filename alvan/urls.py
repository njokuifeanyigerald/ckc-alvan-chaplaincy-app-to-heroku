
from django.urls import path
from .views import(
HomeView, choir_view, marrige_list_view,baptism_list_view, baptism_detail_view,cmo_view,cwo_view,
marriage_detail_view,altar_view, block_rosary_view, readings_view,readings_detail_view,announcement_view,announcement_detail_view,
MarriageSearchView,BaptismSearchView
)

app_name = "alvan"
urlpatterns = [
    path('marriage_search/', MarriageSearchView.as_view(), name="marriage_search"),
    path('baptism_search/', BaptismSearchView.as_view(), name="baptism_search"),
    path('marriage/', marrige_list_view, name="marriage_list"),
    path('baptism/', baptism_list_view, name="baptism_list"),
    path('marriage/<int:id>/', marriage_detail_view, name="marriage_details"),
    path('baptism/<int:id>/', baptism_detail_view, name="baptism_details"),
    path('choir/', choir_view, name="ckc_home"),
    path('cmo/', cmo_view, name="ckc_cmo"),
    path('cwo/', cwo_view, name="ckc_cwo"),
    path('block_rosary/', block_rosary_view, name="ckc_block_rosary"),
    path('altar_server/', altar_view, name="ckc_home"),
    path('', HomeView.as_view(), name="ckc_home"),
    path('readings/', readings_view, name="readings_list"),
    path('announcement/', announcement_view, name="announcement_list"),
    path('readings/<int:id>/', readings_detail_view, name="readings_details"),
    path('announcement/<int:id>/', announcement_detail_view, name="announcement_details"),
]
