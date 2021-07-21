from rest_framework import permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken

from accounts.serializers.user import ListCreateUserSerializer, UserSerializer
from accounts.models.user import User


class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = ListCreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": ListCreateUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        })

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ListCreateUserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = ListCreateUserSerializer


class UserMe(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)
