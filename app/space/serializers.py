from rest_framework import serializers

from space.models import Space


class SpaceSerializer(serializers.ModelSerializer):
    """Serializer for space objects"""

    class Meta:
        model = Space
        fields = (
            'id',
            'title',
            'max_people',
            'min_people',
            'max_price',
            'min_price',
            'days_per_week',
            'link',
            'has_place',
        )
        read_only_fields = ('id',)


class SpaceDetailSerializer(SpaceSerializer):
    """Serializer for space details"""


class SpaceImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images for a space"""

    class Meta:
        model = Space
        fields = ('id', 'image')
        read_only_fields = ('id',)
