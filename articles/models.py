from django.db import models
from django.utils import timezone

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Технологии'),
        ('science', 'Наука'),
        ('sports', 'Спорт'),
        ('politics', 'Политика'),
        ('business', 'Развлечения'),
        ('other', 'Другое'),
    ]

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    author = models.CharField(max_length=100, verbose_name="Автор")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='other',
        verbose_name="Категория"
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_category_display(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)