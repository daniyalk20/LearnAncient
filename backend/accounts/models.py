from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
	default_language = models.ForeignKey(
		"languages.Language",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name="user_profiles",
	)
	transliteration_on = models.BooleanField(default=False)
	font_size = models.PositiveIntegerField(default=16)
	reading_direction = models.CharField(
		max_length=3,
		choices=(
			("ltr", "Left to Right"),
			("rtl", "Right to Left"),
		),
		default="ltr",
	)

	def __str__(self) -> str:
		return f"Profile for {self.user.username}"

