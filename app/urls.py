
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name= 'index'),
    path('portfolio_details/',views.portfolio_details,name='portfolio_details'),
    path('test/',views.test,name='test'),
    path('login_view/',views.login_view,name='login_view'),
    path('contact/',views.contact, name='contact'),
    path('thankyou/',views.thankyou, name='thankyou')
]
