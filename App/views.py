from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, UserActivity
from .forms import UserProfileForm

@login_required
def dashboard_view(request, username):


    if request.user.username != username:
        return redirect('dashboard', username=request.user.username)
   
   
    user_profile = get_object_or_404(UserProfile, username=username)


   
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard', username=user_profile.username) 
    else:
        form = UserProfileForm(instance=user_profile)

 
    activities = UserActivity.objects.filter(user=user_profile).order_by('-timestamp')

 
    context = {
        'user_profile': user_profile,
        'form': form,
        'activities': activities, 
           'activity_count': activities.count(),
    }

    return render(request, 'dashboard/dashboard.html', context)




@login_required
def redirect_to_dashboard(request):
  
  return redirect('dashboard', username=request.user.username)



# def default_view(request):
#     return render(request, 'dashboard/default.html') 