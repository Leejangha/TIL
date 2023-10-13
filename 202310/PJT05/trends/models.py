from django.db import models
from django.utils import timezone

# Create your models here.
class Keyword(models.Model):
    word = models.CharField(max_length=50, unique=True)  # 키워드 이름
    description = models.TextField(blank=True)  # 키워드 설명, 선택사항

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"


class Trend(models.Model):
    keyword = models.CharField(max_length=100, default="기본값")
    search_period = models.CharField(max_length=10, default="all")
    search_results_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now())
    is_active = models.BooleanField(default=True)  # 활성 여부
    
    def __str__(self):
        return f"{self.name} - {self.search_period}"

    class Meta:
        verbose_name = "Trend"
        verbose_name_plural = "Trends"
