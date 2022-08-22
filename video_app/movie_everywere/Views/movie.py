from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from movie_everywere.Serializers import MovieSerializer
from movie_everywere.models import Movie
from movie_everywere.Custom_Exceptions import Exceptions


class MovieViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    @action(methods=['get'], detail=False, url_path='get_all_movie')
    def get_list_movie(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response({"data": serializer.data})

    @action(methods=['get'], detail=False, url_path='director')
    def get_filter_genres(self, request, *args, **kwargs):
        id_direct = kwargs.get('pk')
        if id_direct:
            serializer = self.serializer_class(self.queryset.filter('director'==id_direct))
        else:
            return Exceptions.GanreNotFound()
        return Response({'data': serializer.data})


