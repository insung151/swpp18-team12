from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from club.user_rating.models import UserRating


rating_fields = [
    'overall', 'operation', 'facility',
    'newcomer', 'compulsory', 'meetfreq',
    'age', 'friendliness', 'alcohol',
]


@receiver(post_save, sender=UserRating)
def update_club_rating_save(sender, **kwargs):
    instance = kwargs['instance']
    fields_dict = {}
    if not kwargs.get('raw', False):
        for field in rating_fields:
            if kwargs.get('create', True):
                fields_dict[field] = getattr(instance, field)
            else:
                fields_dict[field] = getattr(instance, field)\
                                     - getattr(instance, f'__original_{field}')
    instance.club.clubrating.add(**fields_dict)


@receiver(post_delete, sender=UserRating)
def update_club_rating_delete(sender, **kwargs):
    instance = kwargs['instance']
    fields_dict = {}
    for field in rating_fields:
        fields_dict[field] = - getattr(instance, field)
    instance.club.clubrating.add(**fields_dict)
