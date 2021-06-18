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
        logger.error(type(info.context.FILES.dict()['file']))

        return UploadMutation(success=True)

