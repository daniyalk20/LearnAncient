from django.db import models
from django.contrib.auth.models import User


class ProgressEvent(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progress_events")
	event_type = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	metadata = models.JSONField(default=dict, blank=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self) -> str:
		return f"{self.user.username} - {self.event_type}"

