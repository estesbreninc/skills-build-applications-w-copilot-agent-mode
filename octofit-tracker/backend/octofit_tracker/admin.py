from django.contrib import admin
from .models import Team, Activity, Workout, Leaderboard, UserTeam

admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Workout)
admin.site.register(Leaderboard)
admin.site.register(UserTeam)
