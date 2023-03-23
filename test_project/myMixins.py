

class CreateListModelMixin(object):

    def get_serializer(self, *args, **kwargs):
        """ Если принят массив, то установить many=True для сериализатора"""
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)

