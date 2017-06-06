"""Employee object"""

__all__ = ["employee_object"]

# Employee object to store information.
def employee_object():
    """
    Example:
    {
       "id": 1,
       "first_name": "Josef",
       "last_name": "Hroch",
       "dep_id": 5,
       "birth_date": "20.08.1986"
    }
    """

    employee = {"id": None,
                "first_name": "",
                "last_name": "",
                "dep_id": None,
                "birth_date": ""}
    return employee
