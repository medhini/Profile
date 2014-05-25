from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from time import time
from FileCheck import ContentTypeRestrictedFileField

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

import logging
logr = logging.getLogger(__name__)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    Follow = models.BooleanField(default=False)
    About_me = models.CharField(max_length=90)
    """picture = models.FileField(upload_to=get_upload_file_name)
    ContentTypeRestrictedFileField(upload_to='static/assets/uploaded_files/', content_types=['image/jpeg','image/png', 'image/bmp', 'image/gif'],max_upload_size=5242880,blank=True, null=True)"""

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        up = UserProfile.objects.create(user=kwargs.get('instance'))
        logr.debug("UserProfile created: %s" % up)
