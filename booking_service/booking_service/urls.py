from django.urls import path
from booking.views import seatSave, seatUpdate

urlpatterns = [
    path('rest/', seatSave),
    path('rest/<int:sid>/', seatUpdate, name='seat-update'),
]
