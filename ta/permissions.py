from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)


class IsCandidateUser(BasePermission):
    message = '구직자만 지원 가능합니다.'
    """
    usertype이 "candidate"일 때만 인가
    """
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response = {
                "detail": "로그인한 사용자만 이용가능합니다.",
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if request.method == 'GET':
            if user.is_authenticated and request.method in self.SAFE_METHODS:
                return True

            return False

        if request.method == 'POST':
            if user.is_authenticated and user.user_type == "candidate":
                return True

        return bool(request.user and user.user_type == "candidate")

        if request.method == 'PUT':
            if user.is_authenticated and user.user_type == "candidate":
                return True

        return bool(request.user and user.user_type == "candidate")


