from django.db import models
from django.utils.translation import gettext as _



class User(models.Model):
    name=models.CharField(max_length=40,verbose_name=_("name"),help_text="نام خود را وارد کنید")


    def __str__(self) -> str:
        return self.name

        
class Category(models.Model):
    CATEGORY_CHOICES=[
        ("sp","SPORT"),
        ("si","SIENCE"),
        ("ec","ECONOMIC"),
        ("po","POLITIC"),
        ("cu","CULTURAL")
        ]
    title=models.CharField(null=True,max_length=2,verbose_name=_("title"),help_text="موضوع موردنظر خود را انتخاب نمایید",choices=CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.title





class Question(models.Model):
    title=models.TextField(verbose_name=_("title"),help_text="متن سوال را وارد نمایید")
    cat=models.ForeignKey(Category,related_name="Questocat",on_delete=models.CASCADE)
    cs1=models.CharField(max_length=255,null=True,default=1)
    cs2=models.CharField(max_length=255,null=True,default=2)
    cs3=models.CharField(max_length=255,null=True,default=3)
    cs4=models.CharField(max_length=255,null=True,default=4)
    answer_choice=[
        ("A","A)"),
        ("B","B)"),
        ("C","C)"),
        ("D","D)")
    ]
    select=models.CharField(max_length=1,verbose_name=_("select"),null=True,choices=answer_choice)
    
    

    def __str__(self) -> str:
        return self.title






class History(models.Model):
    user=models.IntegerField(null=True)
    quiz=models.JSONField(null=True)
    point=models.IntegerField(default=0,null=True)

    def __str__(self) -> str:
        return str(self.id)


