from django.db import models
# for user profiles usage
from django.contrib.auth.models import User
# slug for our profile and blog
from django.template.defaultfilters import slugify
# can add rich text filed to our blog and profile
from ckeditor.fields import RichTextField


# for coding and key skills columns in index profile page
class Skill(models.Model):

    # name of the skill
    name = models.CharField(max_length=20, blank=True, null=True)
    # score in form of sliding bar of the skill score
    score = models.IntegerField(default=80, blank=True, null=True)
    # images for each key skill
    image = models.FileField(blank=True, null=True, upload_to="skills")
    # if True is a skill else is a coding skill
    is_key_skill = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    # returns a skill name
    def __str__(self):
        return self.name


# creating only for one user profile
class UserProfile(models.Model):

    # user field
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image field (make use of Pillow), will create a folder "avatar" where media file will be saved
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    # uploaded to "cv" directory
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    # returns firstname and lastname of user model
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


# For contact Page
class ContactProfile(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    def __str__(self):
        return f'{self.name}'


# Testimonial on home page
class Testimonial(models.Model):

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    # if true would show the person's testimonial otherwise not
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]

    def __str__(self):
        return self.name


# To access Media files and save them in media directory
class Media(models.Model):

    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    # custom save() method
    def save(self, *args, **kwargs):
        # if url esists then is_image validation becomes false
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    def __str__(self):
        return self.name


# for portfolio page
class Portfolio(models.Model):

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    # A Slug is basically a short label for something, containing only letters, numbers, underscores or hyphens.
    # They’re generally used in URLs.
    # A "slug" is a way of generating a valid URL, generally using data already obtained.
    # it is created from the title by down-casing all letters, and replacing spaces by hyphens -
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # we slugify i.e. all letters become small-case and spaces join and become _
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


# same as portfolio page
class Blog(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    def __str__(self):
        return self.name
