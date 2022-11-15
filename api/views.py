from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.models import User, Categories, Post, Comment
from api.permissions import IsAdminOrReadOnly, IsOwnerOrReadAndCreateOnly
from api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer, CategoriesSerializer, PostSerializer, CommentSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        print(serializer.data.get('id'))
        return Response(serializer.data)
    
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data.get('first_name'))
            if serializer.validated_data.get('first_name') == '':
                return Response("User first name cannot be empy")
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
class CategoriesViewSet(ModelViewSet):
    serializer_class = CategoriesSerializer 
    queryset = Categories.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published']

class PostViewset(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)  
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'user', 'slug', 'category__title']

class CommentViewset(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']
    filterset_fields = ['post']