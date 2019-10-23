from drf_haystack.viewsets import HaystackViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework_extensions.cache.mixins import ListCacheResponseMixin
from goods import constants
from goods.models import SKU
from goods.pagenations import StandardPageNumPagination
from goods.serializers import SKUSerializer, SKUIndexSerializer


class HotSKUListView(ListCacheResponseMixin, ListAPIView):
    """
    热销商品, 使用缓存扩展
    """
    serializer_class = SKUSerializer
    pagination_class = StandardPageNumPagination

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return SKU.objects.filter(category_id=category_id, is_launched=True).order_by('-sales')[:constants.HOT_SKUS_COUNT_LIMIT]


class SKUListView(ListAPIView):
    """
    商品列表数据
    """
    serializer_class = SKUSerializer
    pagination_class = StandardPageNumPagination

    # 通过定义过滤后端 ，来实行排序行为
    filter_backends = [OrderingFilter]
    # OrderingFilter过滤器要使用ordering_fields 属性来指定字段排序
    ordering_fields = ('create_time', 'price', 'sales')

    def get_queryset(self):
        categroy_id = self.kwargs.get("category_id")
        return SKU.objects.filter(category_id=categroy_id, is_launched=True)


class SKUSearchViewSet(HaystackViewSet):
    """
    SKU搜索
    """
    index_models = [SKU]

    serializer_class = SKUIndexSerializer
