# models are translated into database tables, model name become database name and fields become its columns
# each object saved become each row of that table
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
    # images for each key skill will be uploaded to skills folder inside mediafiles directory (created automatically)
    # when uploaded in skill admin page
    image = models.FileField(blank=True, null=True, upload_to="skills")
    # True if is a skill else is a coding skill
    is_key_skill = models.BooleanField(default=False)

    # What a class Meta is, if you're familiar with HTML, meta is just data about something, a web page,
    # or a database table. It doesn't alter the function of the item, it just tells about the data.
    # In HTML, the keywords and description content in the head tag is meta data. It just tells us about the page.
    # In Django, we use meta data about a database table to tell Django things about the database table.
    class Meta:
        # verbose_name_plural: defines the plural name for the object
        # If this isn’t given, Django will use verbose_name + "s".
        # verbose_name and verbose_name_plural:
        # If you're familiar with database tables in Django, you know that the table name should be declared to be a
        # singular form, because in the admin page of Django, it ends with pluralizing the table name.
        # This is because a table is really a representation of objects. So if you declare name such as Comment,
        # it really is a collection of Comments (so Django automatically pluralizes it in the admin page once the
        # database table is created and registered).
        #
        # By default, Django adds a 's' to a table name in the admin page.
        #
        # However, this doesn't always work. For example, if a database table called 'Child',
        # the plural of 'Child' is really 'Children', not 'Childs'.
        # If you create a database table called 'Child' and register it in the admin.py file and go to the admin page,
        # you'll see 'Childs'.
        # So there is a way in Django, you can explicitly declare what the singular form of the database objects
        # should be and what the plural form of the database objects should be.
        # And this can be done by using verbose_name and verbose_name_plural attributes.
        verbose_name_plural = 'Skills'
        # verbose_name is pretty much the equivalent of the label attribute for forms.
        # verbose_name is what is used to give labels to forms.
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
    # uploaded to "cv" directory for uploading files (cv/resume)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    # returns first-name and last-name of user model
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
        # The default ordering for the object, for use when obtaining lists of objects.
        # This is a tuple or list of strings and/or query expressions.
        # Each string is a field name with an optional “-” prefix, which indicates descending order.
        # Fields without a leading “-” will be ordered ascending. Use the string “?” to order randomly.
        # Ordering is not a free operation. Each field you add to the ordering incurs a cost to your database.
        # Each foreign key you add will implicitly include all of its default orderings as well.
        # If a query doesn’t have an ordering specified, results are returned from the database in an unspecified order.
        # A particular ordering is guaranteed only when ordering by a set of fields that uniquely identify each object
        # in the results. For example, if a name field isn’t unique, ordering by it won’t guarantee objects with the
        # same name always appear in the same order.
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
    # RichTextField is being used by ckeditor
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
        return "/portfolio/%s/" % self.slug


# same as portfolio page
class Blog(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    # RichTextField is generally used for storing paragraphs that can store any type of data.
    # Rich text is the text that is formatted with common formatting options, such as bold, italics, images, URLs
    # that are unavailable with plain text.
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

    # Define a get_absolute_url() method to tell Django how to calculate the canonical URL for an object.
    # To callers, this method should appear to return a string that can be used to refer to the object over HTTP.
    def get_absolute_url(self):
        return "/blog/%s/" % self.slug


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
