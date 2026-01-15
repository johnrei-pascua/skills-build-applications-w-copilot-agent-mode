from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        user = User.objects.create_user(email='test@example.com', username='testuser', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='test@example.com', activity_type='Run', duration=10)
        self.assertEqual(activity.activity_type, 'Run')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user_email='test@example.com', points=50)
        self.assertEqual(lb.points, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do 10 pushups')
        self.assertEqual(workout.name, 'Pushups')
