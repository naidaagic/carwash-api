from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from wash.models.washing_step import WashingStep
from wash.serializers.washing_step import WashingStepSerializer


class WashingStepList(APIView):
    """
    List all washing steps, or create a new washing step.
    """

    def get(self, request, format=None):
        washing_step = WashingStep.objects.all()
        serializer = WashingStepSerializer(washing_step, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WashingStepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WashingStepDetail(APIView):
    """
    Retrieve, update or delete a washing step instance.
    """

    def get_object(self, pk):
        try:
            return WashingStep.objects.get(pk=pk)
        except WashingStep.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        washing_step = self.get_object(pk)
        serializer = WashingStepSerializer(washing_step)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        washing_step = self.get_object(pk)
        serializer = WashingStepSerializer(
            washing_step, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        washing_step = self.get_object(pk)
        washing_step.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
