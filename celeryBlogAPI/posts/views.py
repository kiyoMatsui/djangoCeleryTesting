# posts/views.py
from rest_framework import generics, permissions

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from rest_framework.response import Response
from .tasks import taskshort, tasklong

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def list(self, request):
            # Note the use of `get_queryset()` instead of `self.queryset`
            queryset = self.get_queryset()
            serializer = PostSerializer(queryset, many=True)
            taskshort.delay()
            tasklong.delay()
            return Response(serializer.data)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
