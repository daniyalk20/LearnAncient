from django.db import models


class Language(models.Model):
	code = models.CharField(max_length=50, unique=True)
	name = models.CharField(max_length=100)
	direction = models.CharField(
		max_length=3,
		choices=(
			("ltr", "Left to Right"),
			("rtl", "Right to Left"),
		),
		default="ltr",
	)
	script = models.CharField(max_length=100)

	def __str__(self) -> str:
		return self.name


class LanguagePack(models.Model):
	language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="packs")
	version = models.CharField(max_length=20)
	features = models.JSONField(default=dict)
	is_active = models.BooleanField(default=True)

	class Meta:
		unique_together = ("language", "version")

	def __str__(self) -> str:
		return f"{self.language.code} {self.version}"

