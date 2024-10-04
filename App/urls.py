from django.urls import include, path
from .views import dashboard_view, redirect_to_dashboard
# ,
# default_view

urlpatterns = [
    path('dashboard/<str:username>/', dashboard_view, name='dashboard'), 
    path('dashboard/', redirect_to_dashboard, name='redirect_to_dashboard'), 
       path('accounts/', include('django.contrib.auth.urls')),
        # path('', default_view, name='default'), 
]
