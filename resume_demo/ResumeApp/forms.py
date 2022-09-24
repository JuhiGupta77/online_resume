from django import forms
from .models import ContactProfile

# A widget is Django’s representation of an HTML input element.
# The widget handles the rendering of the HTML, and the extraction of data from a
# \ GET/POST dictionary that corresponds to the widget.
# need to explicitly define the widget we want to assign to a field.


# contact details to display contact in html page
class ContactForm(forms.ModelForm):
    # below are the details what will be rendered in html page
    # class name is the class-name of the form in html frontend-template (we dont actually need them)
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': '*Full name..',
                                                                                        'class': 'form-control'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Email..',
                                                                                          'class': 'form-control'}))
    message = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(attrs={'placeholder': '*Message..',
                                                                                           'class': 'form-control',
                                                                                           'rows': 6}))

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message',)
