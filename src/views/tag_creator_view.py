from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
    in charge of interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        # Business rule logic
        print('Estou na minha view')
        # http return
        return HttpResponse(status_code=200,body={"Hello":"World"})
