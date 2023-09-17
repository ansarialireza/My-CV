from django.urls import path
from .views import Index,ContactFormView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', ContactFormView.as_view(), name='submit_contact_form'),
]
