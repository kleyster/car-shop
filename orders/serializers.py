from rest_framework import serializers


class ApplicationFormSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ["id", "full_name", "phone_number", "comment", "city", "product"]

        extra_kwargs = {
            "id": {"read_only": True},
            "product": {"read_only": True},
        }