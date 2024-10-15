from middleware.cors import add_cors_middleware
from middleware.log_request import init_log_request_middleware
from middleware.black_list import init_black_list_middleware

def init_middleware(app):
    add_cors_middleware(app)
    init_log_request_middleware(app)
    init_black_list_middleware(app)

__all__ = ["init_middleware"]