from django.urls import path
from . import views
urlpatterns=[
    path('',views.Home,name='Home'),
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('index/',views.index,name='index'),
    path('royal/',views.royal,name='royal'),
    path('pulsar/',views.pulsar,name='pulsar'),
    path('hunter350/',views.hunter350,name='hunter350'),
    path('hondadio/',views.hondadio,name='hondadio'),
    path('yamaha/',views.yamaha,name='yamaha'),
    path('RX/',views.RX,name='RX'),
    path('orders/',views.orders,name='orders'),
    path('show_orders/',views.show_orders,name='show_orders'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('tvs/',views.tvs,name='tvs'),
    path('ktm/',views.ktm,name='ktm'),
]

