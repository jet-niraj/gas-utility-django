from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ServiceRequest, Customer
from .forms import ServiceRequestForm, UserRegistrationForm

def home(request):
    return render(request, 'service_requests/home.html')

@login_required
def create_request(request):
    if request.user.is_staff:
        messages.error(request, "Admins cannot create service requests.")
        return redirect('service_requests:home')

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            messages.success(request, 'Service request created successfully!')
            return redirect('service_requests:request_detail', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_request.html', {'form': form})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    # Check if user has permission to view this request
    if not request.user == service_request.customer:
        messages.error(request, "You don't have permission to view this request.")
        return redirect('service_requests:home')
    
    return render(request, 'service_requests/request_detail.html', {
        'service_request': service_request,
    })

@login_required
def request_list(request):
    if request.user.is_staff:
        messages.error(request, "Admins cannot view service requests.")
        return redirect('service_requests:home')

    requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'service_requests/request_list.html', {'requests': requests})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('service_requests:home')  
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
