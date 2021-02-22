from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from pages import views


router = routers.DefaultRouter()
router.register(r"experts", views.ExpertViewSet)
router.register(r"meetings", views.MeetingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
