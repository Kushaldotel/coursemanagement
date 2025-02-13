from rest_framework import serializers
from django.contrib.auth import get_user_model

StudentUser = get_user_model()

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = ['email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = StudentUser.objects.create(**validated_data)
        user.set_password(password)  # Hash password before saving
        user.save()
        return user
