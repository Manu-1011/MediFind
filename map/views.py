from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
def home(request):
    return render(request,'home.html')
@login_required
def tracking_page(request):
    return render(request,'tracking_page.html')
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('tracking_page')
        else:
            return render(request,'login.html')
    return render(request,'login.html')
def logout_page(request):
    logout(request)
    return render(request,'login.html')
    
def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return render(request,'login.html')
    
    return render(request,'register.html')


class hsv(View):
    def get(self, request):
        state_param = request.GET.get('state', None)
        district_param = request.GET.get('district', None)
        specialties = request.GET.getlist('specialties')
        

        try:
            hospitals = Hospital.objects.all()

            # Filter by state if provided
            if state_param:
                hospitals = hospitals.filter(district__state__name__icontains=state_param)
            
            # Filter by district if provided
            if district_param:
                hospitals = hospitals.filter(district__name__icontains=district_param)
            
            # Filter by specialties if provided
            if specialties:
                hospitals = hospitals.filter(specialty__name__in=specialties).distinct()

            # Prepare data for JSON response
            data = [
                {
                    "name": hospital.name,
                    "address": hospital.address,
                    "latitude": hospital.latitude,
                    "longitude": hospital.longitude,
                    "specialties": [s.name for s in hospital.specialty.all()],
                    "district": hospital.district.name,
                    "state": hospital.district.state.name,
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

class StateListView(View):
    def get(self, request):
        states = State.objects.all()
        data = [{"id": state.id, "name": state.name} for state in states]
        return JsonResponse(data, safe=False)

class DistrictListView(View):
    def get(self, request):
        state_id = request.GET.get('state_id')
        districts = District.objects.filter(state_id=state_id)
        data = [{"id": district.id, "name": district.name} for district in districts]
        return JsonResponse(data, safe=False)


