from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import get_doc
from rest_framework import serializers


class SwaggerSchema(AutoSchema):
    def get_summary(self):
        method_mapping = {
            'GET': 'Информация про',
            'POST': 'Создание',
            'PUT': 'Обновление',
            'PATCH': 'Обновление',
            'DELETE': 'Удаление',
        }
        serializer = self.get_request_serializer()
        try:
            model = serializer.Meta.model._meta
        except AttributeError:
            return None
        model_description = model.verbose_name or model.getdoc
        start_summary = method_mapping.get(self.method)
        return f'{start_summary} {model_description}'

    def get_description(self):
        """ override this for custom behaviour """
        serializer = self.get_request_serializer()
        try:
            model = serializer.Meta.model
            model_doc = model.__doc__
        except AttributeError:
            model_doc = None
        action_or_method = getattr(self.view, getattr(self.view, 'action', self.method.lower()), None)
        view_doc = get_doc(self.view.__class__)
        action_doc = get_doc(action_or_method)
        return action_doc or view_doc or model_doc

    def _get_serializer_field_meta(self, field, direction):
        meta = super()._get_serializer_field_meta(field=field, direction=direction)
        if isinstance(field, serializers.ChoiceField):
            description = meta.get('description', '') + '\n\n Choices:\n'
            values = '\n'.join([f'* `{name} - {normalized}`' for name, normalized in field.choices.items()])
            # values = '\n' + values
            description = description + values
            meta['description'] = description
        return meta
