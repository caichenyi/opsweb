from django.db import models

# Create your models here.

class OpsPerm(models.Model):

    class Meta:
        permissions = (
            ('user_manage', '用户管理'),
            ('group_manage', '用户组管理'),
        )