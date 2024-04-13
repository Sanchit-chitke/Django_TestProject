from django.db import models

class FirstModel(models.Model):
    first_field = models.CharField(max_length=100)

    def __str__(self):
        return self.first_field

class SecondModel(models.Model):
    first_model = models.ForeignKey(FirstModel, on_delete=models.CASCADE)
    second_field = models.CharField(max_length=100)

    def __str__(self):
        return self.second_field


class ThirdModel(models.Model):
    second_model = models.ForeignKey(SecondModel, on_delete=models.CASCADE)
    third_field = models.CharField(max_length=100)

    def __str__(self):
        return self.third_field

