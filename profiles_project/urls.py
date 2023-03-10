from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/profiles/', include('profiles_api.urls')),
    path('api/flight/', include('flight_api.urls'))
]
