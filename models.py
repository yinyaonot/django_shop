# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    detail_url = models.CharField(max_length=200)
    order = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banner'


class Category(models.Model):
    cate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Navigation(models.Model):
    nav_id = models.AutoField(primary_key=True)
    nav_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'navigation'


class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    order_code = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    mobile = models.CharField(max_length=11)
    user_message = models.CharField(max_length=255)
    create_date = models.DateTimeField(blank=True, null=True)
    pay_date = models.DateTimeField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    confirm_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    uid = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'order'


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    cate = models.ForeignKey(Category, models.DO_NOTHING)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'property'


class PropertyValue(models.Model):
    pro_value_id = models.AutoField(primary_key=True)
    property_id = models.IntegerField()
    shop_id = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'property_value'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=4000)
    create_date = models.DateTimeField(blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING)
    uid = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'review'


class Shop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255)
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    promote_price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    cate = models.ForeignKey(Category, models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop'


class ShopCar(models.Model):
    car_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    uid = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid')
    oid = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_car'


class ShopImage(models.Model):
    shop_img_id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_image'


class SubMenu(models.Model):
    sub_menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    cate = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sub_menu'


class SubMenu2(models.Model):
    sub_menu2_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sub_menu = models.ForeignKey(SubMenu, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sub_menu2'


class UserProfile(models.Model):
    uid = models.AutoField(primary_key=True)
    icon = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    desc = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_profile'
