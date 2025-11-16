from django.db import models
from datetime import date


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=500)
    choices = models.JSONField()  # list of strings
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    
class DailyQuestion(models.Model):
    date = models.DateField(unique=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    @staticmethod
    def get_today():
        today = date.today()
        q = Question.objects.order_by("?").first()
        if not q:
            raise ValueError("No questions available. Add some first!")
        dq, created = DailyQuestion.objects.get_or_create(
            date=today,
            defaults={"question": q}
        )
        return dq