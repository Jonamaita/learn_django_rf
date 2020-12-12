"""
Foo serializers
"""
from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer users.
    """

    class Meta:
        """
        Class meta
        """

        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer group.
    """

    class Meta:
        """
        Class meta
        """

        model = Group
        fields = ["url", "name"]
