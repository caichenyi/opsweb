from django.db import models

# Create your models here.

class SqlInfo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField(null=True)
    status = models.IntegerField(null=True)
    submiter = models.CharField(max_length=64)
    drop = models.CharField(max_length=64)
    dev_reviewer = models.CharField(max_length=64)
    dba_reviewer = models.CharField(max_length=64)
    intergrator = models.CharField(max_length=64)
    submit_time = models.DateTimeField(null=True)
    intergrate_time = models.DateTimeField(null=True)

    def __str__(self):
        tpl = '<SqlInfo:[id={id}, title={title}, content={content}, status={status}, submiter={submiter}, ' \
              'drop={drop}, dev_reviewer={dev_reviewer}, dba_reviewer={dba_reviewer}, intergrator={intergrator}, ' \
              'submit_time={submit_time}, intergrate_time={intergrate_time}]>'
        return tpl.format(id=self.id, title=self.title, content=self.content, status=self.status, submiter=self.submiter,
                          drop=self.drop, dev_reviewer=self.dev_reviewer, dba_reviewer=self.dba_reviewer, intergrator=self.intergrator,
                          submit_time=self.submit_time, intergrate_time=self.intergrate_time)