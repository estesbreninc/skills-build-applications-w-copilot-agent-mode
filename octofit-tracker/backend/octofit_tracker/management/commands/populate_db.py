from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        for user in User.objects.all():
            if user.pk:
                user.delete()
        for obj in app_models.Team.objects.all():
            if obj.pk:
                obj.delete()
        for obj in app_models.Activity.objects.all():
            if obj.pk:
                obj.delete()
        for obj in app_models.Leaderboard.objects.all():
            if obj.pk:
                obj.delete()
        for obj in app_models.Workout.objects.all():
            if obj.pk:
                obj.delete()
        for obj in app_models.UserTeam.objects.all():
            if obj.pk:
                obj.delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams with string IDs
        marvel_id = 'team_marvel'
        dc_id = 'team_dc'
        marvel = app_models.Team.objects.create(team_id=marvel_id, name='Marvel')
        dc = app_models.Team.objects.create(team_id=dc_id, name='DC')

        # Create Users (Superheroes)
        users_data = [
            {'username': 'ironman', 'email': 'ironman@marvel.com'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com'},
            {'username': 'batman', 'email': 'batman@dc.com'},
            {'username': 'superman', 'email': 'superman@dc.com'},
        ]
        users = []
        for u in users_data:
            user = User.objects.create_user(username=u['username'], email=u['email'], password='password')
            users.append(user)

        # Assign users to teams
        app_models.UserTeam.objects.create(user_email=users[0].email, team_id=marvel_id)
        app_models.UserTeam.objects.create(user_email=users[1].email, team_id=marvel_id)
        app_models.UserTeam.objects.create(user_email=users[2].email, team_id=dc_id)
        app_models.UserTeam.objects.create(user_email=users[3].email, team_id=dc_id)

        # Create Activities
        for user in users:
            app_models.Activity.objects.create(user_email=user.email, type='run', duration=30, distance=5)
            app_models.Activity.objects.create(user_email=user.email, type='cycle', duration=60, distance=20)

        # Create Workouts
        app_models.Workout.objects.create(workout_id='workout_morning', name='Morning Cardio', description='A quick morning run and cycle')
        app_models.Workout.objects.create(workout_id='workout_strength', name='Strength Training', description='Pushups and squats')

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team_id=marvel_id, points=100)
        app_models.Leaderboard.objects.create(team_id=dc_id, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
