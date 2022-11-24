from django import forms
from .models import ContactProfile

# A widget is Django’s representation of an HTML input element.
# The widget handles the rendering of the HTML, and the extraction of data from a
# \ GET/POST dictionary that corresponds to the widget.
# need to explicitly define the widget we want to assign to a field.


# A ModelForm:
# contact details to display contact in html page
class ContactForm(forms.ModelForm):
    # below are the details what will be rendered in html page
    # class name is the class-name of the form in html frontend-template (we don't actually need them)
    # reason 'name' field's max length is 100 as in modelform of ContactProfile, name is set to 100 likewise others.
    # we are not using 'class': 'form-control' inside our widget declaration as we are not using it in our templates
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': '*Full name..'}))
    # max_length=254 is standard for email field
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
    message = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(attrs={'placeholder': '*Message..',
                                                                                           'rows': 6}))

    class Meta:
        # model which this class represents is ContactProfile
        model = ContactProfile
        # field which we want to render is name, email and message
        fields = ('name', 'email', 'message',)
