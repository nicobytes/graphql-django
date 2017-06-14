from graphene import ObjectType, Schema
from django.contrib.auth.models import User

from api.schemas.user_schema import UsersQuery
from tasks.query import TasksAppQuery

class Query(TasksAppQuery, UsersQuery,   ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = Schema(query=Query)