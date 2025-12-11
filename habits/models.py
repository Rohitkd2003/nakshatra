from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class HabitTemplate(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(HabitTemplate, on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return f"{self.template.title} - {self.user}"


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    log_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.habit} - {self.log_date}"
