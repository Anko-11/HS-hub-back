from werkzeug.exceptions import HTTPException

class APIException(HTTPException):
    code = 500   #http状态码
    message = "fail!"  #状态描述信息
    status_code = 9999 # 程序状态
    def __init__(self, message=None, code=None, status_code = None):
        if message:
            self.message = message
        if code:
            self.code = code
        if status_code:
            self.status_code = status_code
        super(APIException, self).__init__()
    def get_body(self, environ = None, scope = None) -> str:
        body = dict(
            message = self.message,
            code = self.status_code
        )
        import json
        content = json.dumps(body)
        return content

    def get_headers(self, environ = None, scope = None,) :
        return [('content-Type', 'application/json')]

#自定义异常类
class APIAuthorizedException(APIException):
    message = "API授权认证失败"
    status_code = 10002
    code = 401

class FormValidateException(APIException):
    message = "表单验证失败"
    status_code = 10003

class TokenFailException(APIException):
    message = "token不合法，验证失败"
    status_code = 10005
    code = 401

class AuthorizedFailException(APIException):
    message = "认证失败"
    status_code = 10002
    code = 401
