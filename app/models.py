from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    number_of_students = models.IntegerField(default=0)
    price = models.FloatField()
    duration = models.IntegerField()
    # Uncomment and define the Teacher model if needed
    # teachers = models.ManyToManyField(Teacher)
    video = models.FileField(upload_to='media/courses')
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)

    def duration_of_video(self):
        # Implement the actual logic if needed
        pass

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
    rating = models.CharField(max_length=1, choices=RatingChoices.choices, default=RatingChoices.Zero)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.name} - {self.course.title}'
