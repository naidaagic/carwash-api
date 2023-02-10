import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from wash.models.bill import Bill
from wash.models.user import User
from wash.models.washing_program import WashingProgram
from wash.models.washing_step import WashingStep


class TestBill(APITestCase):
    def setUp(self):
        self.wash = WashingStep.objects.create(type="wash")
        self.foam = WashingStep.objects.create(type="foam")
        self.program = WashingProgram.objects.create(name="Regular", price=19.95)
        self.program.washing_steps.set([self.wash, self.foam])
        self.user = User.objects.create(
            name="Alice Bobby",
            email="alice@bobby.com",
            address="Alice From the Block 98",
            phone_number="+38762001002",
        )
        self.bill = Bill.objects.create(
            user=self.user,
            washing_program=self.program,
            price=self.program.price,
            price_after_discount=self.program.price,
        )
        self.valid_bill = {"user": self.user.id, "washing_program": self.program.id}

    def test__pass_get_bill(self):
        response = APIClient().get(path=reverse("bill_list"))
        bill = Bill.objects.count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(bill, 1)

    def test__pass_post_bill(self):
        response = APIClient().post(
            path=reverse("bill_list"),
            data=json.dumps(self.valid_bill),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test__fail_post_bill(self):
        response = APIClient().post(
            path=reverse("bill_list"),
            data=json.dumps({}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test__pass_get_single_bill(self):
        response = APIClient().get(
            path=reverse("bill_detail", kwargs={"pk": self.bill.id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__pass_put_single_bill(self):
        response = APIClient().put(
            path=reverse("bill_detail", kwargs={"pk": self.bill.id}),
            data=json.dumps({"price": 100.95}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
