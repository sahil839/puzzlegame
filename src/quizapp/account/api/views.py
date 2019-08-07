# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from account.api.serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class UserViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id) if self.action == 'current' else super().get_object()

    @action(methods=['get'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

class AuthenticationCheckAPIView(APIView):
    permission_classes = (AllowAny,)
    """
        get:
        Returns the authentication status code and message for current request.
    """

    def get(self, request, *args, **kwargs):
        authenticated = request.user.is_authenticated
        data = {
            'message': 'Authorized' if authenticated else 'Unauthorized'
        }
        status_code = status.HTTP_200_OK if authenticated else status.HTTP_401_UNAUTHORIZED
        return Response(data, status=status_code)