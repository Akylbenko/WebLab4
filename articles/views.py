from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request):
        articles = self.get_queryset()
        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            serializer = self.get_serializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response(
                {"error": "Статья не найдена"},
                status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(
                {"error": "Статья не найдена"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
            return Response(
                {"message": "Статья успешно удалена"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Article.DoesNotExist:
            return Response(
                {"error": "Статья не найдена"},
                status=status.HTTP_404_NOT_FOUND
            )