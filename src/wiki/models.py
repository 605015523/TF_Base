# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class TfPics(models.Model):
    pic_id = models.AutoField(primary_key=True)
    external_id = models.IntegerField()
    title = models.CharField(max_length=40, blank=True, null=True)
    type = models.CharField(max_length=5)
    tag = models.CharField(max_length=40, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tf_pics'

    def __str__(self):
        return self.title


class TfRoles(models.Model):
    role_id = models.AutoField(primary_key=True)
    name_en = models.CharField(unique=True, max_length=60)
    name_ch = models.CharField(max_length=60, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    series = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tf_roles'

    def __str__(self):
        return self.name_en + ' -- ' + self.name_ch

class TfStory(models.Model):
    story_id = models.AutoField(primary_key=True)
    external_id = models.IntegerField()
    story = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tf_story'

    def __str__(self):
        return self.story_id


class TfToys(models.Model):
    toy_id = models.AutoField(primary_key=True)
    role_id = models.IntegerField()
    title = models.CharField(max_length=40, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    version = models.CharField(max_length=40, blank=True, null=True)
    vender = models.CharField(max_length=20, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tf_toys'

    def __str__(self):
        return self.title
