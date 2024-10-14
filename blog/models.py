from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from markdownx.models import MarkdownxField # type: ignore
# Create your models here.
MONTHS = (
    ('فروردین', 'farvardin'),
    ('اردیبهشت', 'ordibehesht'),
    ('خرداد', 'khordad'),
    ('تیر', 'tir'),
    ('مرداد', 'mordad'),
    ('شهریور', 'shahrivar'),
    ('مهر', 'mehr'),
    ('آبان', 'aban'),
    ('آذر', 'azar'),
    ('دی', 'dey'),
    ('بهمن', 'bahman'),
    ('اسفند', 'esfand'),
)
PHRASES = (
    ('آموزش خرید و فروش طلا', 'آموزش خرید و فروش طلا'),
    ('سرمایه گذاری با طلا', 'سرمایه گذاری با طلا'),
    ('بورس و بازار جهانی', 'بورس و بازار جهانی'),
    ('دانستنی طلا', 'دانستنی طلا'),
    ('سکه طلا', 'سکه طلا'),
)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Blog_author",on_delete=models.CASCADE)
    text = MarkdownxField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    blogid = models.UUIDField(default=uuid.uuid4,primary_key=True,
                              unique=True,editable=False)
    blog_image = models.ImageField()
    day = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    month = models.CharField(choices=MONTHS, max_length=50)
    year = models.IntegerField()
    view_count = models.PositiveIntegerField(default=0)
    subject  = models.CharField(choices=PHRASES, max_length=50,default="دانستنی طلا")
    def __str__(self):
        return self.title
    

class Blog_author(models.Model):
    name = models.CharField(max_length=200)
    authorid = models.UUIDField(default=uuid.uuid4,primary_key=True,
                              unique=True,editable=False)
    discription = models.TextField(null=True,blank=True)
    author_img = models.ImageField()
    def __str__(self):
        return self.name
    

class Blog_review(models.Model):
    blog = models.ForeignKey("Blog",on_delete=models.CASCADE,related_name='reviews')
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    reviewid = models.UUIDField(default=uuid.uuid4,primary_key=True,
                              unique=True,editable=False)
    review_text = models.TextField()
    

    def __str__(self):
        return self.username
    

class Blog_rating(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField( validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0)
    rated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog.title} - {self.rating}"