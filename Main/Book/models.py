from django.db import models
from django_jalali.db import models as jmodel
from Book.validators import validatedPrice


class Book(models.Model):
    book_name = models.CharField(max_length=100, verbose_name='نام کتاب')
    number_page = models.IntegerField(verbose_name='تعداد صفحات')
    created = jmodel.jDateTimeField(auto_created=True, verbose_name='تاریخ ایجاد')
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150, verbose_name='اسلاگ')
    discount = models.PositiveIntegerField(blank=True, null=True, verbose_name='تخفیف')
    unit_price = models.PositiveIntegerField(validators=[validatedPrice], verbose_name='قیمت واحد')
    is_available = models.BooleanField(default=True, verbose_name='در دسترس است')
    part_of_book = models.TextField(verbose_name='بخشی از کتاب', null=True, blank=True)
    about_book = models.TextField(verbose_name='درباره کتاب', null=True, blank=True)
    publisher = models.ForeignKey('Publisher', models.PROTECT, 'publisher_books', verbose_name='ناشر')
    author = models.ForeignKey('Author', models.PROTECT, 'author_books', verbose_name='نویسنده')
    genre = models.ManyToManyField('Genre')
    parent_category = models.ForeignKey('ParentCategory', models.PROTECT, 'parent_cat_book',
                                        verbose_name='دسته بندی اصلی')
    child_category = models.ManyToManyField('ChildCategory')


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100)
    manager = models.CharField(max_length=50)
    about_publisher = models.TextField()
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150, verbose_name='اسلاگ')


class Author(models.Model):
    COUNTRIES = (
        ('IRAN', 'ایرانی'),
        ('FRANCH', 'فرانسوی'),
        ('RUSSIAN', 'روسی')
    )

    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=60, verbose_name='نام خانوادگی')
    birthday = jmodel.jDateField(verbose_name='تاریخ تولد')
    from_country = models.CharField(choices=COUNTRIES, default='IRAN', verbose_name='از کشور', max_length=30)
    about_author = models.TextField(verbose_name='زندگینامه')
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150, verbose_name='اسلاگ')


class Genre(models.Model):
    genre_name = models.CharField(max_length=30, verbose_name='نام ژانر')
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150, verbose_name='اسلاگ')


class ParentCategory(models.Model):
    parent_category_name = models.CharField(max_length=20, verbose_name='نام دسته بندی اصلی')
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=150, verbose_name='اسلاگ')
    is_available = models.BooleanField(default=True, verbose_name='در دسترس')

    # def __str__(self):
    #     return self.parent_category_name


class ChildCategory(models.Model):
    parent = models.ForeignKey('ParentCategory', models.PROTECT, 'childToParentCategory', verbose_name='دسته بندی والد')
    child_category_name = models.CharField(max_length=20, verbose_name='نام دسته ی فرزند')
    is_available = models.BooleanField(default=True, verbose_name='در دسترس')
