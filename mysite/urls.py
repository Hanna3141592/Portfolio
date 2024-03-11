
from django.contrib import admin
from django.urls import include, path
from django.conf import settings  # Add this line
from django.conf.urls.static import static  
urlpatterns = [
    path("admin/", admin.site.urls),
   path("", include("index.urls")),  
    path("contact/", include("sendemail.urls")),
    path("resume/", include("CV.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)