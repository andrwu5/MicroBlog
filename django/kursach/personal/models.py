from django.db import models


# PRIORITY = [
#     ("H", "Высокий"),
#     ("M", "Средний"),
#     ("L", "Низкий"),
# ]

# class Question(models.Model):
#     title = models.CharField(verbose_name = 'Заголовок', max_length=50)
#     question = models.TextField(verbose_name = 'Вопрос', max_length=500)
#     priority = models.CharField(verbose_name = 'Приоритет', max_length=1, choices=PRIORITY)    


#     def _str_(self):
#         return self.title

#     class Meta:
#         verbose_name = "Вопрос"
#         verbose_name_plural = "Вопрос"
