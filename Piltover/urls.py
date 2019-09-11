from django.contrib import admin
from django.urls import path, include

from velkoz.urls import router as velkoz_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('velkoz/', include(velkoz_router.urls))
]
