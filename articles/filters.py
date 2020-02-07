#import django_filters
#from articles.models import Article
#
#class ArticleFilter(django_filters.FilterSet):

    #creation_date_start = django_filters.NumberFilter()
    #creation_date_end = django_filters.NumberFilter()
    #sentiment_score_min = django_filters.NumberFilter()
    #sentiment_score_max = django_filters.NumberFilter()

    #publisher = django_filters.CharFilter(field_name='publisher', lookup_expr='iexact')
    #categories = django_filters.CharFilter(field_name='categories', lookup_expr='iexact')

    #creation_date = models.DateTimeField(default=utils.timezone.now)
    #sentiment_score = models.FloatField(null=True)

#    pub = django_filters.ModelMultipleChoiceFilter(queryset=Article.objects.all())

#    class Meta:
#        model = Article
#        fields = ['pub']
        #fields = ['publisher']
        #fields = ['publisher', 'categories']


# Implement filter so that you can do:
# http: // positive-front.azurewebsites.net/api/articles?topic=business&num=10
# 
