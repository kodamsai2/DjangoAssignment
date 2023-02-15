import graphene
from graphene_django.types import DjangoObjectType
from .models import Banks, Branches

class BranchesType(DjangoObjectType):
    class Meta:
        model = Branches

class Query(object):
    branches = graphene.List(BranchesType)

    def resolve_all_branches(self, info, **kwargs):
        return Branches.objects.all()