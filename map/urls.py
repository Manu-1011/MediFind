from django.urls import path
from .views import*

urlpatterns = [
    path('', home, name='home'),
    path('tracking',tracking_page , name='tracking_page'),
    path('api/hospitals/', hsv.as_view(), name='hospital_by_specialty'),
    path('api/specialties/', SpecialtyListView.as_view(), name='specialty_list'),
    path('api/states/', StateListView.as_view(), name='state_api'),
    path('api/districts/', DistrictListView.as_view(), name='district_api'),
    path('login/', login_page, name='login'), 
    path('logout/', logout_page, name='logout'),
    path('registration/', register_page, name='registration'),

]