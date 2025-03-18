from django.shortcuts import render
from.models import *
from django.http import JsonResponse
from django.views import View
def home(request):
    return render(request,'home.html')

def tracking_page(request):
    return render(request,'tracking_page.html')


class hsv(View):
    def get(self, request):
        specialties = request.GET.getlist('specialties')
    
        
        try:
            if specialties:
                hospitals = Hospital.objects.filter(specialty__name__in=specialties).distinct()
            
            else:
                hospitals = Hospital.objects.all()

            data = [
                {
                    "name": hospital.name,
                    "address": hospital.address,
                    "latitude": hospital.latitude,
                    "longitude": hospital.longitude,
                    "specialties": [s.name for s in hospital.specialty.all()]
                }
                for hospital in hospitals
            ]
            
            return JsonResponse(data, safe=False)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
class SpecialtyListView(View):
    def get(self, request):
        specialties = Specialty.objects.all().values('name')
        return JsonResponse(list(specialties), safe=False)