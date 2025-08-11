from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    author = models.ForeignKey(to="Author", on_delete=models.PROTECT, related_name="books")
    genre = models.ManyToManyField(to="Genre")

    def __str__(self):
        return self.title
