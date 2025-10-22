from contextvars import ContextVar
# not recomended, but Im going to try it anyway
current_user = ContextVar("current_user", default=None)