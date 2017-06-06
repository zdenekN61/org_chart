"""Department object"""

__all__ = ["department_object"]

# Department object to store information.
def department_object():
    """
    Example:
    {
       "id": 1,
       "parent_id": None,
       "dep_name": "Delivery",
       "dep_city": "Brno",
       "sub-dep-id": [5,6]
    }
    """

    department = {"id": None,
                 "parent_id": None,
                 "dep_name": "",
                 "dep_city": "",
                 "sub_dep_id": []}
    return department
