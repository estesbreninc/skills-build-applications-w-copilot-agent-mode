from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard, UserTeam

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(team_id='team_test', name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password')
        self.assertEqual(user.email, 'testuser@example.com')

    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='testuser@example.com', type='run', duration=10, distance=2.5)
        self.assertEqual(activity.type, 'run')

    def test_workout_creation(self):
        workout = Workout.objects.create(workout_id='workout_test', name='Test Workout', description='Test Desc')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team_id='team_test', points=50)
        self.assertEqual(leaderboard.points, 50)

    def test_userteam_creation(self):
        userteam = UserTeam.objects.create(user_email='testuser@example.com', team_id='team_test')
        self.assertEqual(userteam.team_id, 'team_test')
