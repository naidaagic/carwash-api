import json
from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from wash.models.washing_program import WashingProgram
from wash.models.washing_step import WashingStep


class TestWashingProgramView(APITestCase):
    def setUp(self):
        self.wash = WashingStep.objects.create(type="wash")
        self.foam = WashingStep.objects.create(type="foam")
        self.valid_program = {
            "name": "program_name",
            "price": 19.95,
            "washing_steps": [self.wash.id, self.foam.id],
        }
        self.program = WashingProgram.objects.create(name="Regular", price=19.95)
        self.program.washing_steps.set([self.wash, self.foam])

    def test__pass_get_washing_program(self):
        response = APIClient().get(path=reverse("washing_program_list"))
        washing_program = WashingProgram.objects.count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(washing_program, 1)

    def test__pass_post_washing_program(self):
        response = APIClient().post(
            path=reverse("washing_program_list"),
            data=json.dumps(self.valid_program),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test__fail_post_washing_program(self):
        response = APIClient().post(
            path=reverse("washing_program_list"),
            data=json.dumps({}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test__pass_get_single_washing_program(self):
        response = APIClient().get(
            path=reverse("washing_program_detail", kwargs={"pk": self.program.id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__pass_put_single_washing_program(self):
        response = APIClient().put(
            path=reverse("washing_program_detail", kwargs={"pk": self.wash.id}),
            data=json.dumps(
                {"name": "Foamy", "price": 10.99, "washing_steps": [self.foam.id]}
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
