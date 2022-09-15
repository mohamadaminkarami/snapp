class CreateListModelMixin(object):
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            print("data", kwargs.get('data'))
            kwargs['many'] = True

        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)
