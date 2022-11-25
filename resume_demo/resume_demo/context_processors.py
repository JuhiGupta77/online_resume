# added User model
from django.contrib.auth.models import User


def project_context(request):
    # first(), which takes a query set and returns the first element, or None if the query set was empty.
    context = {
        'me': User.objects.first(),
    }
    return context