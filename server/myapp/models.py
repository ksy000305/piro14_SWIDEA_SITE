from django.db import models
from django.urls import reverse



class Devtool(models.Model):
    name = models.CharField(max_length=100, verbose_name=">> 이름")
    kind = models.CharField(max_length=100, verbose_name=">> 종류")
    desc = models.TextField(blank=True, verbose_name=">> 개발툴 설명")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("myapp:devtool_detail", kwargs={"pk": self.pk})
    

class Idea(models.Model):
    title = models.CharField(max_length=100, verbose_name=">> 아이디어명")
    image = models.ImageField(upload_to="idea_main_image", verbose_name=">> 대표 사진")
    content = models.TextField(blank=True, verbose_name=">> 아이디어 설명")
    interest = models.IntegerField(default=0, verbose_name=">> 아이디어 관심도")

    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, verbose_name=">> 예상 개발툴")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("myapp:idea_detail", kwargs={"pk": self.pk})
    

