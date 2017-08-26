from django.conf import settings


def from_settings(_request):
    return {
        'ADMIN_RIBBON_TEXT': settings.ADMIN_RIBBON['TEXT'],
        'ADMIN_RIBBON_COLOR': settings.ADMIN_RIBBON['COLOR'],
    }
