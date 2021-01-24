from django.db import models




class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class products(models.Model):
    bookname = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)



