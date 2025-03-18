from django.urls import path
from .views import*

urlpatterns = [
    path('', home, name='home'),
    path('tracking',tracking_page , name='tracking_page'),
    path('api/hospitals/', hsv.as_view(), name='hospital_by_specialty'),
    path('api/specialties/', SpecialtyListView.as_view(), name='specialty_list'),

]