from django.db import models
from users.models import Student, Employee
from django.utils import timezone

class Assignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    assessment_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.student} {self.lecturer} {self.assessment_date}"
