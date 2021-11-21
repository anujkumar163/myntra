"""myntra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('home/', views.home), 
    path('page0/', views.webpage0, name='webpage0'),
    path('page1/', views.webpage1,name='webpage1'),
    path('page2/', views.webpage2,name='webpage2'),
    path('add_product/', views.add_product),
    path('cartdetail/', views.cartdetails),
    path('signup/', views.signup),
    path('login/', views.login_call),
    path('seller/', include('seller.urls')),
    path('logout/', views.logout_call),
    path('buyer/', include('buyer.urls')),
    path('app2/', include('app2.urls')),
   
    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)















