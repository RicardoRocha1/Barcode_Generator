from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import CreateTagController

class TagCreatorView:
    '''
    in charge of interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = CreateTagController()

        body = http_request.body
        product_code = body["product_code"]

        # Business rule logic
        formatted_response = tag_creator_controller.create(product_code)
        # http return
        return HttpResponse(status_code=200,body= formatted_response)
