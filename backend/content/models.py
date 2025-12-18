from django.db import models


class Manuscript(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image_url = models.URLField(blank=True)

	def __str__(self) -> str:
		return self.title


class Passage(models.Model):
	language_pack = models.ForeignKey(
		"languages.LanguagePack",
		on_delete=models.CASCADE,
		related_name="passages",
	)
	manuscript = models.ForeignKey(
		Manuscript,
		on_delete=models.CASCADE,
		related_name="passages",
		null=True,
		blank=True,
	)
	reference = models.CharField(max_length=200)
	content = models.TextField(help_text="Surface text of the passage")
	is_published = models.BooleanField(default=True)

	def __str__(self) -> str:
		return self.reference


class Lemma(models.Model):
	language = models.ForeignKey(
		"languages.Language",
		on_delete=models.CASCADE,
		related_name="lemmas",
	)
	lemma = models.CharField(max_length=100)
	gloss = models.CharField(max_length=255, blank=True)

	class Meta:
		unique_together = ("language", "lemma")

	def __str__(self) -> str:
		return self.lemma


class Morphology(models.Model):
	language = models.ForeignKey(
		"languages.Language",
		on_delete=models.CASCADE,
		related_name="morphologies",
	)
	tag = models.CharField(max_length=50)
	description = models.CharField(max_length=255)

	class Meta:
		unique_together = ("language", "tag")

	def __str__(self) -> str:
		return self.tag


class Token(models.Model):
	passage = models.ForeignKey(Passage, on_delete=models.CASCADE, related_name="tokens")
	index = models.PositiveIntegerField(help_text="Position of token in passage")
	text = models.CharField(max_length=100)
	lemma = models.ForeignKey(Lemma, on_delete=models.SET_NULL, null=True, blank=True)
	morphology = models.ForeignKey(
		Morphology,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)
	gloss = models.CharField(max_length=255, blank=True)
	audio_url = models.URLField(blank=True)

	class Meta:
		unique_together = ("passage", "index")
		ordering = ["index"]

	def __str__(self) -> str:
		return f"{self.text} ({self.passage.reference})"

