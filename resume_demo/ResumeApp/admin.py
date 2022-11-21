from django.contrib import admin
from .models import (UserProfile, ContactProfile, Testimonial, Media, Portfolio, Blog, Certificate, Skill)


# The register decorator
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    # Set list_display to control which fields are displayed on the change list page of the admin.
    # If you don’t set list_display, the admin site will display a single column that displays the __str__()
    # representation of each object.
    # list_display will allow us to display fields that we want in the admin page
    list_display = ('id', 'timestamp', 'name',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    # read only field should be slug, which could be a blog link,
    # so that it remains the same each time the blog link is created
    readonly_fields = ('slug',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')
