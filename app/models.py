from django.db import models

class Teacher(models.Model):
    class RatingChoices(models.TextChoices):
        Beginner = 'Beginner',
        Junior = 'Junior',
        Middle = 'Middle ',
        Senior = 'Senior',
        Expert = 'Expert'

    full_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=100, choices=RatingChoices.choices, default=RatingChoices.Junior.value)
    twitter_link = models.CharField(max_length=150, null=True, blank=True)
    facebook_link = models.CharField(max_length=150, null=True, blank=True)
    linkedin_link = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)

    def __str__(self):
        return self.full_name

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    education = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='authors/')

    def __str__(self):
        return self.full_name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    auther_id = models.ManyToManyField(Author, related_name='blogs')

    def __str__(self):
        return self.title

class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    number_of_students = models.IntegerField(default=0)
    price = models.FloatField()
    duration = models.IntegerField()
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    video = models.FileField(upload_to='courses/')
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def hours(self):
        if self.duration >= 60:
            hours = self.duration // 60
            return hours

    @property
    def minutes(self):
        if self.duration >= 60:
            minutes = self.duration % 60
            return minutes

    objects = models.Manager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    class RatingChoices(models.TextChoices):
        Zero = '0'
        One = '1'
        Two = '2'
        Three = '3'
        Four = '4'
        Five = '5'

    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    is_published = models.BooleanField(default=False)
    rating = models.CharField(max_length=100, choices=RatingChoices.choices, default=RatingChoices.Zero.value)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
