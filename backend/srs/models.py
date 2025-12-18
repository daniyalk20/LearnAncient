from django.db import models
from django.contrib.auth.models import User


class ReviewItem(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_items")
	token = models.ForeignKey(
		"content.Token",
		on_delete=models.CASCADE,
		related_name="review_items",
	)
	easiness = models.FloatField(default=2.5)
	interval = models.PositiveIntegerField(default=1, help_text="Interval in days")
	repetitions = models.PositiveIntegerField(default=0)
	due = models.DateField()

	def __str__(self) -> str:
		return f"ReviewItem({self.user.username}, {self.token_id})"

