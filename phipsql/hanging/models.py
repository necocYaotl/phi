from django.db import models

class Word(models.Model):
    word = models.CharField(max_length = 42)
    rgt = models.IntegerField()
    wrg = models.IntegerField()

    def __str__(self):
        return self.word


class Right(models.Model):
    word = models.ForeignKey(Word)
    letter = models.CharField(max_length = 1)
    state = models.BooleanField(default = False)

    def __str__(self):
        return self.letter


class Wrong(models.Model):
    word = models.ForeignKey(Word)
    letter = models.CharField(max_length = 1)

    def __str__(self):
        return self.letter


class Responds(models.Model):
    situation = models.CharField(max_length = 100)
    saying = models.TextField()
    ratio = models.IntegerField()

    def __str__(self):
        return self.saying


class Terminal(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
