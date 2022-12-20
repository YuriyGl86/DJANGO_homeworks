from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        creator = self.context['request'].user
        open_advertisements_count = creator.advertisement_set.filter(status='OPEN').count()

        new_open_advertisement = False

        if self.context["request"].method in ['PATCH']:
            new_status = data.get('status')
            advertisement_pk = self.context['view'].kwargs['pk']
            old_status = Advertisement.objects.get(pk=advertisement_pk).status
            if new_status == 'OPEN' and old_status != 'OPEN':
                new_open_advertisement = True

        elif self.context["request"].method in ['POST']:
            new_advertisement_status = data.get('status', 'OPEN')
            if new_advertisement_status == 'OPEN':
                new_open_advertisement = True

        print('число открытых: ', open_advertisements_count)
        print('метод', self.context["request"].method)
        print('открытие нового объявления: ', new_open_advertisement)

        if not new_open_advertisement or new_open_advertisement and open_advertisements_count < 10:
            return data
        else:
            raise ValidationError('Превышено максимальное число активных объявлений')










