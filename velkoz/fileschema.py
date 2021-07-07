from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from graphene_file_upload.scalars import Upload
import graphene
import logging


class UploadMutation(graphene.Mutation):
    class Arguments:
        def __init__(self):
            pass

        file = Upload(required=True)

    success = graphene.Boolean()

    # noinspection PyMethodMayBeStatic
    def mutate(self, info, file, **kwargs):
        logger = logging.getLogger('critical')
        icon = info.context.FILES.dict()['file']
        default_storage.save('static/{0}'.format(icon.name), ContentFile(icon.read()))

        return UploadMutation(success=True)

