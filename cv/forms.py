from django import forms

class ContactForm(forms.Form):
    contactName = forms.CharField(label='Name', max_length=100)
    contactEmail = forms.EmailField(label='Email', max_length=100)
    contactSubject = forms.CharField(label='Subject', max_length=100, required=False)
    contactMessage = forms.CharField(label='Message', widget=forms.Textarea)