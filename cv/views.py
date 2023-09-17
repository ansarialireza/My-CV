from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import ContactForm


class Index(TemplateView):
    template_name='index.html'

# iews.py

# views.py
class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact_form.html'  # Replace with your template path
    success_url = '/success/'  # Replace with the URL where you want to redirect after successful submission

    def form_valid(self, form):
        # Get form data
        name = form.cleaned_data['contactName']
        email = form.cleaned_data['contactEmail']
        subject = form.cleaned_data['contactSubject']
        message = form.cleaned_data['contactMessage']

        # Email settings
        recipient_email = 'user@website.com'  # Replace with the recipient's email
        from_email = f'{name} <{email}>'
        message_body = f'Email from: {name}\nEmail address: {email}\nMessage:\n{message}\n'

        try:
            send_mail(subject, message_body, from_email, [recipient_email], fail_silently=False)
            return JsonResponse({'status': 'OK'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    def form_invalid(self, form):
        # Form validation error
        errors = form.errors.as_json()
        return JsonResponse({'status': 'validation_error', 'errors': errors})
