# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    bookname = models.CharField(db_column='Bookname', unique=True, max_length=255)  # Field name made lowercase.
    original_bookname = models.CharField(db_column='Original_Bookname', max_length=255)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    how_much_charter = models.IntegerField(db_column='How_much_charter')  # Field name made lowercase.
    how_much_translated = models.IntegerField(db_column='How_much_translated', blank=True, null=True)  # Field name made lowercase.
    translate_done = models.IntegerField(db_column='Translate_done')  # Field name made lowercase.
    who_translate = models.ForeignKey('Transletors', models.DO_NOTHING, db_column='Who_translate')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Books'

    def __str__(self):
        return self.bookname


class Journal(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.ForeignKey('Reader', on_delete=models.CASCADE, db_column='Username')  # Field name made lowercase.
    bookname = models.ForeignKey(Books, on_delete=models.CASCADE, db_column='BookName')  # Field name made lowercase.
    page = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Journal'

    def __str__(self):
        return '{0} {1}'.format(self.username, self.bookname)

class Reader(models.Model):
    username = models.CharField(db_column='Username', unique=True, max_length=255)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(db_column='First_name', max_length=255)  # Field name made lowercase.
    second_name = models.CharField(db_column='Second_Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reader'

    def __str__(self):
        return self.username



class Transletors(models.Model):
    username = models.CharField(db_column='Username', unique=True, max_length=255)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(db_column='First_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    second_name = models.CharField(db_column='Second_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    english_level = models.CharField(db_column='English_level', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transletors'

    def __str__(self):
        return self.username


def transaction_post_save_receiver(sender, instance, created, *args, **kwargs):
#     instance.reader.username = instance.username
#     instance.reader.email = instance.email
#     instance.reader.password = instance.password
#     instance.reader.first_name = instance.first_name
#     instance.reader.second_name = instance.second_name
#     instance.reader.username.save()
#     instance.reader.email.save()
#     instance.reader.password.save()
#     instance.reader.first_name.save()
#     instance.reader.second_name.save()
    if created:
        username = instance.username
        email = instance.email
        password = instance.password
        first_name = instance.first_name
        second_name = instance.second_name
        reader = Reader(username = username,email = email, password = password,first_name = first_name,second_name = second_name)
        reader.save()

post_save.connect(transaction_post_save_receiver, sender=Transletors)


def add_new_user_post_save_reader(sender, instance, created, *args, **kwargs):
    if created:
        # user = User(username = instance.username, email = instance.email, password = instance.password,
        #             first_name = instance.first_name, last_name = instance.second_name)
        # user.save()
        user = User.objects.create_user(username=instance.username,
                                        email=instance.email,
                                        password=instance.password)
        user.save()

post_save.connect(add_new_user_post_save_reader, sender=Reader)