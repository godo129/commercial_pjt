from django.db import models
from django.conf import settings

# Create your models here.
class Rent(models.Model):
    tag_choice = [(0, '구매'), (1, '판매')]
    rent_choice = [(0, '월세'), (1, '전세'), (2, '매매')]
    loc_choice = [('강남구', '강남구'), ('강동구', '강동구'), ('강북구', '강북구'), ('강서구', '강서구'), ('관악구', '관악구'),
                  ('광진구', '광진구'), ('구로구', '구로구'), ('금천구', '금천구'), ('노원구', '노원구'), ('도봉구', '도봉구'),
                  ('동대문구', '동대문구'), ('동작구', '동작구'), ('마포구', '마포구'), ('서대문구', '서대문구'), ('서초구', '서초구'),
                  ('성동구', '성동구'), ('성북구', '성북구'), ('송파구', '송파구'), ('양천구', '양천구'), ('영등포구', '영등포구'),
                  ('용산구', '용산구'), ('은평구', '은평구'), ('종로구', '종로구'), ('중구', '중구'), ('중랑구', '중랑구')
                  ]
    title = models.CharField(max_length=50)
    content = models.TextField()
    tag = models.IntegerField(choices=tag_choice, blank=False, default=1)
    rent_type = models.IntegerField(choices=rent_choice, help_text="거래 유형을 선택해주세요", blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(choices=loc_choice, help_text="지역을 선택해주세요", blank=False, default='강남구', max_length=10)
    price = models.IntegerField(help_text="만 원 단위로 적어주세요.", blank=False, default='50')
    