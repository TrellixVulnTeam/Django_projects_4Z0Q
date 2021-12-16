from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=255)
  # pole tekstowe o określonej długości
  content = models.TextField()
  # pole tekstowe o nieokreślonej długości
  published = models.BooleanField(default=False)
  # flaga true/false
  created = models.DateTimeField(auto_now_add=True)
  # data utworzenia - tylko przy utworzeniu
  modified = models.DateTimeField(auto_now=True)
  # data modyfikacji - zawsze po kliknięciu save
  sponsored = models.BooleanField(default=False)
  # post sponsorowany
  author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts")
  # relacja postu z autorem którym jest id usera
  
  def __str__(self):
    # metoda specjalna służąca do przygotowania reprezentacji
    # tekstowej naszego obiektu. Zmiana w widoku jak i w PA
    return f"{self.id} {self.title}"
  
 