from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from .serializers import StudentUserSerializer
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from django.db.models.signals import post_save

StudentUser = get_user_model()

class CreateStudentView(APIView):
    def post(self, request):
        data = request.data
        raw_password = data.get("password")  # Get the raw password

        # Hash the password before saving
        data["password"] = make_password(raw_password)
        serializer = StudentUserSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            user._raw_password = raw_password  # Temporarily attach password before saving
            post_save.send(sender=StudentUser, instance=user, created=True)  # Manually trigger signal
            return Response({"message": "Student created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@staff_member_required  # Ensures only admin users can access the page
def create_student_page(request):
    return render(request, "create_student.html")