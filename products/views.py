from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer 
from django_ratelimit.decorators import ratelimit

# Create your views here.
class ProductPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 300

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()

    category = request.query_params.get('category')
    search = request.query_params.get('search')
    sort_by = request.query_params.get('sort')

    #Filter by category if url has category param
    if category:
        products = products.filter(category=category)

    #Search for a product in all  website or if category is true then inside that category
    if search:
        products = products.filter(
            Q(name__icontains=search)
        )

    #Sort products based on name, price and rating in both asc and desc order
    if sort_by:
        if sort_by == "price_low":
            products = products.order_by('price')
        elif sort_by == "price_high":
            products = products.order_by('-price')
        elif sort_by == "name_asc":
            products = products.order_by('name')
        elif sort_by == "name_desc":
            products = products.order_by('-name')
        elif sort_by == "rating_desc":
            products = products.order_by('-average_rating')
        else:
            products = products.order_by('name')
    
    #Pagination - Send 10 products at a time by adding pages
    paginator = ProductPagination()
    paginated_products = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(paginated_products, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
@ratelimit(key='ip', rate='50/m', method='POST')
def rate_product(request, product_id):
    if getattr(request, 'limited', False):
        return Response({'error': 'Too many rating attempts'}, status=429)
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)
    
    new_rating = request.data.get('rating')
    if new_rating is None:
        return Response({'error':'Rating value missing'}, status=400)
    if new_rating < 1 or new_rating > 5:
        return Response({'error':'Rating must be between 1 and 5'}, status=400)
    
    product.total_no_of_ratings = product.total_no_of_ratings + 1
    product.sum_ratings = product.sum_ratings + new_rating
    product.average_rating = round(product.sum_ratings / product.total_no_of_ratings, 1)
    
    product.save()

    return Response({
        'average_rating': product.average_rating,
        'total_no_of_ratings': product.total_no_of_ratings
    })
