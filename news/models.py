from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=150, verbose_name='Название')
	content = models.TextField(verbose_name='Контент')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
	is_published = models.BooleanField(verbose_name='Опубликовано?', default=True)
	category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
	views = models.IntegerField(verbose_name='Количество просмотров', default=0)

	def get_absolute_url(self):
		return reverse('view_news', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
		ordering = ['-created_at']


class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')

	def get_absolute_url(self):
		return reverse('category', kwargs={'category_id': self.pk})

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['title']




