from django.db import models
from django.conf import settings

# Create your models here.

class Conversation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="conversations"
    )

    title = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    summary_last_message_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversation {self.id}"
    


class Message(models.Model):

    ROLE_CHOICES = [
        ("user", "User"),
        ("assistant", "Assistant"),
        ("system", "System"),
    ]

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages"
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    content = models.TextField(blank=True, null=False)
    image_url = models.URLField(blank=True, null=True)
    tokens = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
    
    def __str__(self):
        return f"{self.role}: {(self.content or '')[:30]}"

