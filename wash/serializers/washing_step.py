from rest_framework import serializers

from wash.models.washing_step import WashingStep


class WashingStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = WashingStep
        fields = ["id", "type"]
