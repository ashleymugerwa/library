from django.conf.urls import url
from . import views

app_name = 'mueni'

urlpatterns = [
    url(r'^add_book/$', views.CashDigital.add_book),
    url(r'^register_member/$', views.CashDigital.register_member),
    url(r'^borrow_book/$', views.CashDigital.borrow_book),
    url(r'^remove_book/$', views.CashDigital.remove_book),
    url(r'^deactivate_member/$', views.CashDigital.deactivate_member),
    url(r'^return_book/$', views.CashDigital().return_book),

]
