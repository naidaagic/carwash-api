from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from wash.models.washing_program import WashingProgram
from wash.serializers.washing_program import WashingProgramSerializer


class WashingProgramList(APIView):
    """
    List all washing programs, or create a new washing program
    """

    def get(self, request, format=None):
        washing_program = WashingProgram.objects.all()
        serializer = WashingProgramSerializer(washing_program, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WashingProgramSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.create(request.data)
            except Exception as exc:
                return Response(
                    f"Must fill out all fields in form.",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WashingProgramDetail(APIView):
    """
    Retrieve, update or delete a washing program instance.
    """

    def get_object(self, pk):
        try:
            return WashingProgram.objects.get(pk=pk)
        except WashingProgram.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        washing_program = self.get_object(pk)
        serializer = WashingProgramSerializer(washing_program)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        washing_program = self.get_object(pk=pk)
        serializer = WashingProgramSerializer(
            washing_program, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.update(instance=washing_program, validated_data=request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        washing_program = self.get_object(pk)
        washing_program.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
