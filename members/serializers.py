from django.contrib.auth.hashers import make_password
from materials.models import Course
from rest_framework import serializers
from .models import Payment, CustomUser


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        ref_name = 'CustomUserSerializer'

    def create(self, validated_data):
        password = validated_data.get('password')

        # Hash the password before saving
        if password:
            hashed_password = make_password(password)
            validated_data['password'] = hashed_password

        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.get('password')

        # Hash the password before saving
        if password:
            hashed_password = make_password(password)
            validated_data['password'] = hashed_password

        user = super().update(instance, validated_data)
        return user


class CourseSubscriptionSerializer(serializers.Serializer):
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
