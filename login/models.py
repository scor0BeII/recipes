from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()

class Recipes(models.Model):
    title = models.CharField("Заголовок", max_length = 128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена продуктов", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Пользователь")
    image = models.ImageField(verbose_name="Изображение", upload_to="recipes/", blank=True, null=True)
    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone, html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return html.format_html("<span style='color:green; font-weight: bold;'> Сегодня в {} </span>", created_time)
        else:
            return self.created_at.strftime("%d.%m.%y в %H:%M:%S")
# Create your models here.
