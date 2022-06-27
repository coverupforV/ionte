from tortoise import models
from tortoise import fields


class Note(models.Model):
    name = fields.CharField(max_length=50, null=False, description="笔记名称")
    date = fields.CharField(max_length=50, null=False, description="笔记时间")
    comment = fields.CharField(max_length=5000, null=False, description="笔记内容")







