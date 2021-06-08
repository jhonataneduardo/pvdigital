from rest_framework import permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken

from accounts.serializers.auth import AuthLoginSerializer
from accounts.serializers.user import UserSerializer


class LoginAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AuthLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
