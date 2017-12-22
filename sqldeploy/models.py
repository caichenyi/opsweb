from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SqlInfo(models.Model):
    db_env = models.IntegerField(null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField(null=True)
    status = models.IntegerField(null=True)
    submiter = models.IntegerField(null=True)
    dropper = models.IntegerField(null=True)
    dev_reviewer = models.IntegerField(null=True)
    dba_reviewer = models.IntegerField(null=True)
    intergrator = models.IntegerField(null=True)
    submit_time = models.DateTimeField(null=True)
    intergrate_time = models.DateTimeField(null=True)

    def __str__(self):
        tpl = '<SqlInfo:[id={id}, title={title}, content={content}, status={status}, submiter={submiter}, ' \
              'drop={drop}, dev_reviewer={dev_reviewer}, dba_reviewer={dba_reviewer}, intergrator={intergrator}, ' \
              'submit_time={submit_time}, intergrate_time={intergrate_time}]>'
        return tpl.format(id=self.id, title=self.title, content=self.content, status=self.status, submiter=self.submiter,
                          drop=self.dropper, dev_reviewer=self.dev_reviewer, dba_reviewer=self.dba_reviewer, intergrator=self.intergrator,
                          submit_time=self.submit_time, intergrate_time=self.intergrate_time)


class DbEnv(models.Model):
    id = models.AutoField(primary_key=True)
    db_env = models.CharField(max_length=64)
    db_name = models.CharField(max_length=64)
    db_host = models.CharField(max_length=64)
    db_port = models.IntegerField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        tpl = '{db_env}'
        return tpl.format(id=self.id, db_env=self.db_env, db_name=self.db_name, db_host=self.db_host, db_port=self.db_port, username=self.username, password=self.password)