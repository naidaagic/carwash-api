from rest_framework import serializers

from wash.models.washing_program import WashingProgram
from wash.models.washing_step import WashingStep
from wash.serializers import attempt_json_deserialize
from wash.serializers.washing_step import WashingStepSerializer


class WashingProgramSerializer(serializers.ModelSerializer):
    washing_steps = WashingStepSerializer(read_only=True, many=True)

    class Meta:
        model = WashingProgram
        fields = ["id", "name", "price", "washing_steps", "created_at"]

        def create(self, validated_data):
            """
            Create and return a new `WashingProgram` instance, given the validated data.
            :param validated_data:
            :return:
            """
            request = self.context["request"]

            name = request.data.get("name")
            name = attempt_json_deserialize(name, expect_type=str)
            validated_data["name"] = name

            price = request.data.get("price")
            price = attempt_json_deserialize(price, expect_type=float)
            validated_data["price"] = price

            steps = request.data.get("washing_steps")
            steps = attempt_json_deserialize(steps, expect_type=list)
            step_objects = []
            for step in steps:
                step_object = WashingStep.objects.get(pk=step)
                if step_object:
                    step_objects.append(step_object)
            validated_data["washing_steps"] = step_objects
            instance = super().create(validated_data)

            return instance

        def update(self, instance: WashingProgram, validated_data):
            """
            Update and return an existing `WashingProgram` instance, given the validated data.
            :param instance:
            :param validated_data:
            :return:
            """
            request = self.context["request"]

            name = request.data.get("name")
            if name:
                name = attempt_json_deserialize(name, expect_type=str)
                validated_data["name"] = name

            price = request.data.get("price")
            if price:
                price = attempt_json_deserialize(price, expect_type=float)
                validated_data["price"] = price

            steps = request.data.get("washing_steps")
            if steps:
                steps = attempt_json_deserialize(steps, expect_type=list)
                step_objects = instance.washing_steps
                for step in steps:
                    step_object = WashingStep.objects.get(pk=step)
                    if step_object:
                        if step_object not in step_objects:
                            step_objects.append(step_object)
                validated_data["washing_steps"] = step_objects
            instance = super().update(instance, validated_data)
            return instance
