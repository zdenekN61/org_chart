"""Show help"""

__all__ = ["show_help"]

# Show help.
def show_help():
    _help = """Supported commands + examples:
               Department 5 -> name of department for ID.
               Count 1 -> number of employees(+sub-departs) for ID.
               People 1 -> names of employees(+sub-departs) for ID.
               Avgage 1 -> average age of employees(+sub-departs) for ID.
               Help -> this help.
               Exit -> the end.
               ----------------------------------------------------------"""
    return _help
