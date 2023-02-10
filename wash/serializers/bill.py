from rest_framework import serializers

from wash.models.bill import Bill
from wash.models.user import User
from wash.models.washing_program import WashingProgram
from wash.serializers import attempt_json_deserialize
from wash.serializers.user import UserSerializer
from wash.serializers.washing_program import WashingProgramSerializer


class BillSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    washing_program = WashingProgramSerializer(read_only=True)

    class Meta:
        model = Bill
        fields = [
            "id",
            "price",
            "price_after_discount",
            "user",
            "washing_program",
        ]

    def create(self, validated_data):
        """
        Create and return a new `Bill` instance, given the validated data.
        :param validated_data:
        :return:
        """
        user = validated_data.get("user")
        user = attempt_json_deserialize(user, expect_type=int)
        user_obj = None
        if user:
            user_obj = User.objects.get(pk=user)
        if user_obj:
            validated_data["user"] = user_obj
        else:
            return None

        washing_program = validated_data.get("washing_program")
        washing_program = attempt_json_deserialize(washing_program, expect_type=int)
        washing_program_obj = None
        if washing_program:
            washing_program_obj = WashingProgram.objects.get(pk=washing_program)
        if washing_program_obj:
            validated_data["washing_program"] = washing_program_obj
        else:
            return None
        validated_data["price"] = washing_program_obj.price

        user_loyalty_level = user_obj.loyalty_level
        num_bills = Bill.objects.filter(user=user).count() + 1
        calc = num_bills // 10 + 1

        new_loyalty_level = None
        if calc != user_loyalty_level and calc <= 10:
            new_loyalty_level = calc

        if new_loyalty_level:
            User.objects.filter(pk=user).update(loyalty_level=new_loyalty_level)

        new_price = washing_program_obj.price * (1 - 0.025 * (user_loyalty_level - 1))
        validated_data["price_after_discount"] = new_price

        instance = super().create(validated_data)

        return instance

    def update(self, instance: Bill, validated_data):
        """
        Update and return an existing `Bill` instance, given the validated data.
        :param instance:
        :param validated_data:
        :return:
        """
        user = validated_data.get("user")
        if user:
            user = attempt_json_deserialize(user, expect_type=int)
            validated_data["user"] = User.objects.get(pk=user)

        price = validated_data.get("price")
        if price:
            price = attempt_json_deserialize(price, expect_type=float)
            validated_data["price"] = price

        washing_program = validated_data.get("washing_program")
        if washing_program:
            washing_program = attempt_json_deserialize(washing_program, expect_type=int)
            validated_data["washing_program"] = WashingProgram.objects.get(
                pk=washing_program
            )

        price_after_discount = validated_data.get("price_after_discount")
        if price_after_discount:
            price_after_discount = attempt_json_deserialize(
                price_after_discount, expect_type=float
            )
            validated_data["price_after_discount"] = price_after_discount

        instance = super().update(instance, validated_data)

        return instance
