from rest_framework import serializers

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def validated(self, attrs):
        title = attrs.get('title')
        title = title.apper()
        attrs['title'] = title
        return attrs

    def validate_description(self, d):
        if len(d)<20:
            raise serializers.ValidationError('Опписание слишком короткое')
        return d
