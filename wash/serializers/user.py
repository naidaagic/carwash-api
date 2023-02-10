from rest_framework import serializers

from wash.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "address",
            "phone_number",
            "loyalty_level",
            "date_joined",
        ]
