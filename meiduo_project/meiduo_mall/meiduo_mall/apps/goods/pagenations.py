from rest_framework.pagination import PageNumberPagination


class StandardPageNumPagination(PageNumberPagination):
    page_size = 35
    page_size_query_param = 'page_size'
    # 前端请求的每页数量上限
    max_page_size = 20
