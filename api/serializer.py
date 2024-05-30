from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Customers



class RegsitrationSerializers(serializers.ModelSerializer):
    password1 =serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ["username","password1","password2","password", "email"]
        read_only_fields =["id", "password"]


    def create(self, validated_data):
        password1 = validated_data.pop("password1")
        password2 = validated_data.pop("password2")
        if password1==password2:
            return User.objects.create_user(**validated_data, password=password1)
        else:
            raise serializers.ValidationError

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"




