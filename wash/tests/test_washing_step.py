import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from wash.models.washing_step import WashingStep


class TestWashingStepView(APITestCase):
    def setUp(self):
        self.valid_step = {"type": "type_name"}
        self.wash = WashingStep.objects.create(type="wash")
        self.foam = WashingStep.objects.create(type="foam")

    def test__pass_get_washing_step(self):
        response = APIClient().get(path=reverse("washing_step_list"))
        washing_steps = WashingStep.objects.count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(washing_steps, 2)

    def test__pass_post_washing_step(self):
        response = APIClient().post(
            path=reverse("washing_step_list"),
            data=json.dumps(self.valid_step),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test__fail_post_washing_step(self):
        response = APIClient().post(
            path=reverse("washing_step_list"),
            data=json.dumps({}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test__pass_get_single_washing_step(self):
        response = APIClient().get(
            path=reverse("washing_step_detail", kwargs={"pk": self.wash.id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__pass_put_single_washing_step(self):
        response = APIClient().put(
            path=reverse("washing_step_detail", kwargs={"pk": self.wash.id}),
            data=json.dumps({"type": "extra foam"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
