from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list_create_view(request):
  if request.method == 'GET':
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
  
  serializer = PostSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save(author= request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail_view(request, pk):
  post = get_object_or_404(Post, pk=pk)

  if request.method == 'GET':
    serializer = PostSerializer(post)
    return Response(serializer.data)
  
  elif request.method in ['PUT', 'PATCH']:
    partial = request.method == 'PATCH'
    serializer = PostSerializer(post, data=request.data, partial=partial)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    post.delete()
    return Response(
      {"message": "Post deleted successfully"},
      status=status.HTTP_204_NO_CONTENT
    )