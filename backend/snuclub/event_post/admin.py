from django.contrib import admin

from event_post.models import EventPost, EventPostComment

admin.site.register(EventPost)
admin.site.register(EventPostComment)
