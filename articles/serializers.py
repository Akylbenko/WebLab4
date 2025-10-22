from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'content', 'author', 'category', 'category_display',
            'created_at', 'updated_at', 'is_published'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'category_display']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Заголовок должен содержать минимум 5 символов")
        return value

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Содержание должно содержать минимум 10 символов")
        return value

    def validate_author(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Имя автора должно содержать минимум 2 символа")
        return value

    def validate_category(self, value):
        valid_categories = ['tech', 'science', 'sports', 'politics', 'entertainment', 'other']
        if value not in valid_categories:
            raise serializers.ValidationError("Неверная категория")
        return value