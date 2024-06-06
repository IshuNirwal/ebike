
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', Home, name='home'),
    path('skylark/', Skylark, name='skylark'),
    path('starling/', Starling, name='starling'),
    path('swallow/', Swallow, name='swallow'),
    path('eagle/', Eagle, name='eagle'),
    path('drake/', Drake, name='drake'),
    path('canary/', Canary, name='canary'),
    path('models/', Models, name='models'),
    path('dealer/', Dealer, name='dealer'),
    path('contact/', Contact, name='contact'),
    path('about/', About, name='about'),
    path('thank-you/', Thank, name='thankyou'),
]


# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)