from rest_framework import serializers
from .models import Profile, UserDataModel, DataModel

class DataModelSummarySerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        model = DataModel
        fields = [
            'pk'
        ]

        read_only_fields = [
            'pk'
        ]


class DataModelDetailSerializer(DataModelSummarySerializer):
    class Meta:
        abstract = True
        model = DataModel
        fields = DataModelSummarySerializer.Meta.fields + [
        ]

        read_only_fields = DataModelSummarySerializer.Meta.fields + [
        ]


class UserDataModelSummarySerializer(DataModelSummarySerializer):
    class Meta:
        abstract = True
        model = UserDataModel
        fields = DataModelSummarySerializer.Meta.fields + [

        ]

        read_only_fields = DataModelSummarySerializer.Meta.read_only_fields + [ 'user'

        ]


class UserDataModelDetailSerializer(DataModelDetailSerializer, UserDataModelSummarySerializer):
    class Meta:
        abstract = True
        model = UserDataModel
        fields = DataModelDetailSerializer.Meta.fields + UserDataModelSummarySerializer.Meta.fields + [
        ]

        read_only_fields = DataModelDetailSerializer.Meta.read_only_fields +\
                           UserDataModelSummarySerializer.Meta.read_only_fields + ['user']


class UserSerializer(UserDataModelDetailSerializer):
    class Meta:
        model = Profile
        fields = ('id' ,'first_name', 'last_name', 'IBAN')
        read_only_fields = ('id',)