from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/')
    description = models.CharField(max_length=1000)
    pub_date = models.DateField()
    instructors = models.ManyToManyField(Instructor)
    is_enrolled = models.BooleanField(default=False)
    total_enrollment = models.IntegerField(default=0)

    def __str__(self):
        return "Name: " + self.name + "," + " Description: " + self.description


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    # Foreign key to lesson
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    # Question text
    question_text = models.CharField(max_length=600)
    # Question grade/mark
    grade = models.IntegerField(default=1)

    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        if all_answers == selected_correct:
            return True
        else:
            return False

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Foreign key to question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Choice text
    choice_text = models.CharField(max_length=600)
    # Boolean field to indicate if this choice is the correct answer
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    # Foreign key to enrollment
    enrollment = models.ForeignKey(User, on_delete=models.CASCADE)
    # Foreign key to lesson  
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    # Selected choices for the submission
    choices = models.ManyToManyField(Choice)
    # Date of submission
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.enrollment.username} for {self.lesson.title}"
