import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from wash.models.user import User


class TestWashingStepView(APITestCase):
    def setUp(self):
        self.valid_user = {
            "name": "user_name",
            "email": "user@user.com",
            "address": "User Avenue 123",
            "phone_number": "123456798",
        }
        self.user = User.objects.create(
            name="Alice Bobby",
            email="alice@bobby.com",
            address="Alice From the Block 98",
            phone_number="+38762001002",
        )

    def test__pass_get_user(self):
        response = APIClient().get(path=reverse("user_list"))
        user = User.objects.count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user, 1)

    def test__pass_post_user(self):
        response = APIClient().post(
            path=reverse("user_list"),
            data=json.dumps(self.valid_user),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test__fail_post_user(self):
        response = APIClient().post(
            path=reverse("user_list"),
            data=json.dumps({}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test__pass_get_single_user(self):
        response = APIClient().get(
            path=reverse("user_detail", kwargs={"pk": self.user.id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__pass_put_single_user(self):
        response = APIClient().put(
            path=reverse("user_detail", kwargs={"pk": self.user.id}),
            data=json.dumps({"loyalty_level": 2}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
