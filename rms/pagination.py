from rest_framework.pagination import PageNumberPagination


# Pagination of 10 item: 
class PageOfTen(PageNumberPagination):
    page_size = 10                          # shows the default amount of data per page
    page_size_query_param = 'page_size'     # allows frontend user to request custom amount of data, bypassing default amount
    max_page_size = 100                     # sets maximum number of data a frontend user can request at once 
    

# Pagination of 20 item: 
class PageOfTwenty(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    
