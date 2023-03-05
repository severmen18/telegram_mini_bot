from django.db import models

# Create your models here.
class Skills(models.Model):
    skill = models.CharField(max_length=256, verbose_name="Название навыка")

    def __str__(self):
        return self.skill
    
    class Meta:
        verbose_name_plural = "скилы"
        verbose_name = "скил"

class Students(models.Model):

    first_name = models.CharField(max_length=210, verbose_name="Имя")
    last_name = models.CharField(max_length=210, verbose_name="Фамилия" )
    age = models.IntegerField(verbose_name="Возраст")
    student_class = models.IntegerField(verbose_name="Класс")
    skils = models.ManyToManyField(Skills, verbose_name="Скилы")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "школьники"
        verbose_name = "школьник"

