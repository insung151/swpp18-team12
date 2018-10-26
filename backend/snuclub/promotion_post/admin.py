from django.contrib import admin

from promotion_post.models import PromotionPost, PromotionPostComment

admin.site.register(PromotionPost)
admin.site.register(PromotionPostComment)
