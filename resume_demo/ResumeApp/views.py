from django.shortcuts import render
# when the form is valid and is saved then message appears saying as Thank You
from django.contrib import messages
from .models import (UserProfile, Blog, Portfolio, Testimonial, Certificate)
# importing generic to use generic views i.e. form views, list views etc. (builtin views)
from django.views import generic
from .forms import ContactForm


# TemplateView: class based generic views to accomplish common tasks.
# It Renders a given template, with the context containing parameters captured in the URL.
# TemplateView should be used when you want to present some information on an HTML page.
# TemplateView should not be used when your page has forms and does creation or update of objects.
# In such cases, FormView, CreateView, or UpdateView is a better option.
# TemplateView is most suitable in the following cases:
# Showing ‘about us’ like pages that are static and hardly need any context.
# Though, it is easy to use context variables with TemplateView.
# Showing pages that work with GET requests and don’t have forms in them.
class IndexView(generic.TemplateView):
    template_name = "ResumeApp/index.html"

    # This method is used to populate a dictionary to use as the template context
    def get_context_data(self, **kwargs):
        # Returns context data for displaying the object
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context


class ContactView(generic.FormView):
    template_name = "ResumeApp/contact.html"
    form_class = ContactForm
    # user will get redirected when the form is valid
    success_url = "/"

    # form valid method
    def form_valid(self, form):
        # save the form instance
        form.save()
        # send the message success
        messages.success(self.request, 'Thank You. We will be in touch Soon.')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "ResumeApp/portfolio.html"
    # django.views.generic.list.ListView provides a builtin way to paginate the displayed list.
    # You can do this by adding a paginate_by attribute to your view class.
    # will show first 2 objects
    paginate_by = 10

    # When you set queryset, the queryset is created only once, when you start your server.
    # On the other hand, the get_queryset method is called for every request.
    # That means that get_queryset is useful if you want to adjust the query dynamically.
    # For example, you could return objects that belong to the current user
    def get_queryset(self):
        # only active portfolios are returned
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "ResumeApp/portfolio-detail.html"


class BlogView(generic.ListView):
    model = Blog
    template_name = "ResumeApp/blog.html"
    paginate_by = 10

    # Used by ListViews - it determines the list of objects that you want to display
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "ResumeApp/blog-detail.html"