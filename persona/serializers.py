from unicodedata import category
from rest_framework import serializers

from persona.models import Answer, Mbti


class AvatarByMbtiSerializer(serializers.Serializer):
    mbti = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=64)
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    description = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048)


class PlaceByMbtiSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    picture = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    loc = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    description = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048)
    mbti = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=64)


class CharactersByMbtiSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    mbti = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=64)
    isFemale = serializers.BooleanField(required=True, allow_null=False)
    category = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    description = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048)


class SubmitAnswersSerializer(serializers.Serializer):
    class Meta:
        model = Answer
        fields = ('user', 'question', 'time', 'answer')


class SubmitCharacterSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
    description = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048)
    mbti = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=64)
    isFemale = serializers.BooleanField(required=True, allow_null=False)
    category_id = serializers.IntegerField(required=True, allow_null=False)


class UpdateCharacterCoverSerializer(serializers.Serializer):
    character_id = serializers.IntegerField(required=True, allow_null=False)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)


class DeleteCharacterSerializer(serializers.Serializer):
    character_id = serializers.IntegerField(required=True, allow_null=False)
