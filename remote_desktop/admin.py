from django.contrib import admin

# Register your models here.
from remote_desktop import models

# 在admin平台注册表
for item in models.__all__:
    admin.site.register(getattr(models, item))
