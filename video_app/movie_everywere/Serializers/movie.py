from rest_framework import serializers
from movie_everywere.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'