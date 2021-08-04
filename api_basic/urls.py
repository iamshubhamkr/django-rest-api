
from django.urls import path,include
# from .views import article_list,article_detail,ArticleAPIView
from .views import ArticleAPIView,ArticleDetail,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')
# urlpatterns = router.urls

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls))
    # path('article/',article_list,name='article'),
    # path('article/',ArticleAPIView.as_view()),
    # path('detail/<int:pk>/',ArticleDetail.as_view()),
    
    # path('generic/',GenericAPIView.as_view())
    # path('generic/article/<int:id>/',GenericAPIView.as_view())


    # path('detail/<int:pk>/',article_detail,name='article_detail')
]