from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from wash.models.bill import Bill
from wash.serializers.bill import BillSerializer


class BillList(APIView):
    """
    List all bills, or create a new bill.
    """

    def get(self, request, format=None):
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BillSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            try:
                bill = serializer.create(request.data)
            except ValueError:
                return Response(
                    "Must choose user and washing program",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(f"Success: {bill.id}", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillDetail(APIView):
    """
    Retrieve, update or delete a bill instance.
    """

    def get_object(self, pk):
        try:
            return Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bill = self.get_object(pk)
        serializer = BillSerializer(bill)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bill = self.get_object(pk)
        serializer = BillSerializer(bill, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(bill, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bill = self.get_object(pk)
        bill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
