from django.shortcuts import HttpResponse

# def my_middleware(get_response):
#     print("One time initialization(fm)")
#
#     def my_function(request):
#         print("this is before view(fm)")
#         response = get_response(request)
#         print("this is after view(fm)")
#         return response
#
#     return my_function
#
#
# class My_cls_middleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time initialization(class)")
#
#     def __call__(self, request):
#         print("this is before view..!!(class)")
#         response = self.get_response(request)
#         print("this is after view..!!()class")
#         return response

class Brothermiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time brother intialization")

    def __call__(self, request):
        print("Before view brother middleware")
        response = self.get_response(request)
        print("After view brother middleware")
        return response


class Fathermiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Father intialization")

    def __call__(self, request):
        print("Before view Father middleware")
        response = self.get_response(request)
        print("After view Father middleware")
        return response


class Mothermiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Mother intialization")

    def __call__(self, request):
        print("Before view Mother middleware")
        response = self.get_response(request)
        print("After view Mother middleware")
        return response
