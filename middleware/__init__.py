from middleware.process_time import add_process_time, log_request
from middleware.cors import add_cors_middleware
_middleware_initialized = False

def init_middleware(app):
    global _middleware_initialized
    if not _middleware_initialized:
        print("Initializing middleware")
        # 通过这个方法可以动态添加中间件
        app.middleware("http")(add_process_time)
        app.middleware("http")(log_request)
        add_cors_middleware(app)
        _middleware_initialized = True
    else:
        print("Middleware already initialized")

__all__ = ["init_middleware"]