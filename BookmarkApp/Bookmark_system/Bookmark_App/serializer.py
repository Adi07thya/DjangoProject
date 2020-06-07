from rest_framework import serializers
from .models import Customer,Bookmark,CustomerBookmark
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

User = get_user_model()

"""   Serializing Model Instances for the representation which we can streamable over the network """

class CustomerSerializer(serializers.ModelSerializer):


    class Meta:
        model   = Customer
        fields  = '__all__'

    def get_status_display(self, obj):
        """status display is the read_only field to serilaized which return the value of the get_status_display method"""

        return obj.get_status_display()



class BookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model    = Bookmark
        fields   = '__all__'

    def get_status_display(self, obj):
        """status display is the read_only field to serilaized which return the value of the get_status_display method"""
        return obj.get_status_display()



class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(source='get_full_name', read_only=True)


    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', )




class CustomerBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model    = CustomerBookmark
        fields   = '__all__'
