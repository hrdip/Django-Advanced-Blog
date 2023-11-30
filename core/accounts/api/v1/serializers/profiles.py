from rest_framework import serializers
from ....models import Profile

    
class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email', read_only=True)
   
    class Meta:
        model = Profile
        fields = ('id','email', 'first_name', 'last_name', 'image', 'description', 'bio',
                   'facebook_profile', 'instagram_profile', 'linkedin_profile')
        read_only_fields = ['email']