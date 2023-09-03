from django.db import models
from django.utils.text import slugify



class category(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    lastname = models.CharField(max_length=50,blank=True, null=True)
    decription = models.CharField(max_length=250, blank=True, null=True)
    longdecription = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category/',null=True,blank=True)
    poster = models.ImageField(upload_to='poster/',null=True,blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name} {self.lastname}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.lastname}"


class quotes(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    color = models.CharField(max_length=15,null=True, blank=True)
    quote = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.quote

