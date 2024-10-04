from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class NoteListCreate(generics.ListCreateAPIView): # List or create
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Enforces JWT token use

    # Needs to be here because user is authenticated
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid(): # checking that all args were valid to make a note
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView): # Generic view built in to django for creating new user/object.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]