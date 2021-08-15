from drf_yasg import openapi

from_date_params = openapi.Parameter(
    'from_date',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='Start date in format "YYYY-MM-DD". Example "2021-08-15"'
)

to_date_params = openapi.Parameter(
    'to_date',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description='Start date in format "YYYY-MM-DD". Example "2021-08-15"'
)