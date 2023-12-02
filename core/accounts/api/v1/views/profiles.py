from rest_framework import generics
from ..serializers.profiles import ProfileSerializer
from ....models import Profile
from django.shortcuts import get_object_or_404


class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
