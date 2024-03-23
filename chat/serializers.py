from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *
from authendications.models import *
from rest_framework import serializers

class UserListserializer(ModelSerializer):
   class Meta:
        model = User
        fields = ['id', 'email', 'first_name','last_name','place','state','district', 'profile_image']

class MessageSerializer(ModelSerializer):
    sender_email = serializers.EmailField(source='sender.email')

    class Meta:
        model = Message
        fields = ['message', 'sender_email']

class AllUserListSerializer(ModelSerializer):
    is_friends = SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'profile_image', 'is_friends']

    def get_is_friends(self, obj):
        user_id = self.context['user_id']
        
        friends_list = FriendsList.objects.filter(user_id=user_id, friends_id=obj.id, is_connected=True).first()
        
        if friends_list:
            return 'connected'
        else:
            pending_request = FriendsList.objects.filter(user_id=user_id, friends_id=obj.id, is_connected=False).first()
            if pending_request:
                return 'pending'
            else:
                return 'not_friends'


class UserDetailSerialzer(ModelSerializer):
    is_friends = SerializerMethodField()
    friends_list = SerializerMethodField()
    friends_count = SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name','last_name','place','state','district','bio', 'profile_image','is_friends','friends_list','friends_count']

    
    def get_is_friends(self, obj):
        user_id = self.context['user_id']
        
        friends_list = FriendsList.objects.filter(user_id=user_id, friends_id=obj.id, is_connected=True).first()
        
        if friends_list:
            return 'connected'
        else:
            pending_request = FriendsList.objects.filter(user_id=user_id, friends_id=obj.id, is_connected=False).first()
            if pending_request:
                return 'pending'
            else:
                return 'not_friends'
    
    def get_friends_list(self, obj):
        user_id = self.context['id']
        friends_list = []
        try:
            queryset = FriendsList.objects.filter(user_id=user_id, is_connected=True).distinct()
            for friendship in queryset:
                friend = User.objects.filter(id=friendship.friends_id.id).values('id', 'email', 'first_name','last_name','place','state','district', 'profile_image').first()
                if friend:
                    friends_list.append(friend)
            return friends_list
        except FriendsList.DoesNotExist:
            return friends_list
    def get_friends_count(self,obj):
        user_id = self.context['id']
        count = 0
        try:
            queryset = FriendsList.objects.filter(user_id=user_id, is_connected=True).distinct()
            count = queryset.count()
            return count
        except FriendsList.DoesNotExist:
            return count