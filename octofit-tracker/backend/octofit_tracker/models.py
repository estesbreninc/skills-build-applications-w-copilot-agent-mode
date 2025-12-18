from djongo import models

class Team(models.Model):
    team_id = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField()    # in km
    timestamp = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    workout_id = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

class Leaderboard(models.Model):
    team_id = models.CharField(max_length=24)
    points = models.IntegerField()

class UserTeam(models.Model):
    user_email = models.EmailField()
    team_id = models.CharField(max_length=24)
