from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('re/', include('pages.urls')),
    # path('re/listings/', include('listings.urls')),
    # path('re/accounts/', include('accounts.urls')),
    # path('re/contacts/', include('contacts.urls')),
    # path('qr/', include('attendees.urls')),
    path('admin/', admin.site.urls),
    path('', include('myapps.urls')),
]
