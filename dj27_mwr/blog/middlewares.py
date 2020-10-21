from django.shortcuts import HttpResponse


class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, *args, **kwargs):
        print("this is process view before view")
        # return HttpResponse("This is before view")
        return None


class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print("exception occured")
        msg = exception
        class_name = exception.__class__.__name__
        print("class: ", class_name)
        print(msg)
        return HttpResponse(msg)


class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print("process templates response from middleware..!!")
        response.context_data['name'] = 'Lucas'
        response.context_data['age'] = 34
        return response
