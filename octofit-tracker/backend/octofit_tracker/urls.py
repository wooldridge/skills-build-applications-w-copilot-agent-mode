"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import JsonResponse
import os
from .views import TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        base_url = "/api/"
    return JsonResponse({
        'activities': base_url + 'activities/',
        'workouts': base_url + 'workouts/',
        'teams': base_url + 'teams/',
        'leaderboard': base_url + 'leaderboard/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/activities/', include(router.urls)),
    path('api/workouts/', include(router.urls)),
    path('api/teams/', include(router.urls)),
    path('api/leaderboard/', include(router.urls)),
]
