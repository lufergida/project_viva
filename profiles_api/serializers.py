from rest_framework import serializers
from profiles_api import models

class ProofSerializer(serializers.Serializer):
    """Serializer for a field in our APIView"""
    name= serializers.CharField(max_length=10)


class UserSerializerTest(serializers.Serializer):
    name = serializers.CharField(max_length=10, required=True)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a object user profiles_api"""
    
    class Meta:
        model= models.UserProfile
        fields =('id', 'email', 'name', 'password')
        
        
    def create(self, validated_data):
        """Create and return a new user profile"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']       
        )
        
        return user
    
    def update(self, instance, validated_data):
        """Update user profile"""
        if 'password' in validated_data:
            password= validated_data.pop('password')
            instance.set_password(password)
            
        return super().update(instance, validated_data)
    
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializer for feed item"""
    
    class Meta:
            model= models.ProfileFeedItem
            fields = ('id', 'user_profile', 'status_text', 'created_on')
            extra_kwargs={'user_profile':{'read_only':True}}
            