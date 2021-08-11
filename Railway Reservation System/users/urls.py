from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('booking/', views.ticketbook, name = 'ticketbook'),
    path('train/',views.train, name = 'train'),
    path('cancel/',views.cancel, name = 'cancel'),
    path('booking/payment',views.payment, name = 'payment'),
    path('/passenger/<int:train_number>',views.passenger, name = 'passenger'),
    path('/passenger/confirm/',views.booking_confirm, name = 'booking_confirm'),
    path('cancel_res/<int:pnr>',views.cancel_reservation,name = 'cancel_reservation'),
    path('history/',views.booking_history,name = 'booking_history'),
]