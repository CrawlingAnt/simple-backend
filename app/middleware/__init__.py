from middleware.process_time import add_process_time, log_request
from middleware.cors import add_cors_middleware


def init_middleware(app):
    # 通过这个方法可以动态添加中间件
    app.middleware("http")(add_process_time)
    app.middleware("http")(log_request)
    add_cors_middleware(app)
   

__all__ = ["init_middleware"]