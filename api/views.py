from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from api.serializer import RegsitrationSerializers, CustomerSerializer
from api.models import Customers
# Create your views here.



class SignupView(CreateAPIView):
    serializer_class = RegsitrationSerializers
    queryset = Customers.objects.all()


class CustomerListandCreateView(ListAPIView, CreateAPIView):
    serializer_class = CustomerSerializer
    queryset  = Customers.objects.all()



class CustomerDeleteUpdateandFetchView(UpdateAPIView, RetrieveAPIView, DestroyAPIView):
    serializer_class = CustomerSerializer
    queryset  = Customers.objects.all()





