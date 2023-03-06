from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    '''
    This is the category database model which consists of the name of
    categories
    '''
    name = models.CharField(max_length=255)

    class Meta:
        '''
        This class we used to set the ordering of categories according
        to ther names and set plural to categories 
        '''
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        '''
        We return the name of the category to be displayed
        '''
        return self.name

class Item(models.Model):

    '''
    This is the item database model
     ___________________________
    |____________Item___________|
    | category: FK              |
    | name: CharField           |
    | description: TF           |
    | price: FloatField         |
    | image: ImageField         |
    | is_sold: BooleanField     |
    | created_by: FK (UserDB)   |
    | created_at: DateTimeField |
    |___________________________|
    '''
    category = models.ForeignKey(Category, related_name='items', on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        Return the name of the item
        '''
        return self.name