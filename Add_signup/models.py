from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=200, unique=True, null=False)
    email = models.EmailField(max_length=254, unique=True, null=False)
    password = models.CharField(max_length=128)

    # Metadat about the class - in this case User class would be pluralised
    # to Userss in Django admin
    class Meta:
        verbose_name_plural = "Users"

    # Define __str__ that will be called when querying e.g. 'Users.objects.all()'
    def __str__(self):
        obj_str = f'ID: {self.id}\n' \
                   f'Username: {self.username}\n' \
                   f'Email: {self.email}\n' \
                   f'Password: {self.password}\n' \

        return obj_str