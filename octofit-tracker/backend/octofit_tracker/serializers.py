from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard, UserTeam

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user_email', 'type', 'duration', 'distance', 'timestamp']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['workout_id', 'name', 'description']

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['id', 'team_id', 'points']

class UserTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTeam
        fields = ['id', 'user_email', 'team_id']
