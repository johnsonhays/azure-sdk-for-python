# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QueryFilter(Model):
    """The filter expression to be used in the export.

    :param and_property: The logical "AND" expression. Must have at least 2
     items.
    :type and_property: list[~azure.mgmt.costmanagement.models.QueryFilter]
    :param or_property: The logical "OR" expression. Must have at least 2
     items.
    :type or_property: list[~azure.mgmt.costmanagement.models.QueryFilter]
    :param not_property: The logical "NOT" expression.
    :type not_property: ~azure.mgmt.costmanagement.models.QueryFilter
    :param dimension: Has comparison expression for a dimension
    :type dimension:
     ~azure.mgmt.costmanagement.models.QueryComparisonExpression
    :param tag: Has comparison expression for a tag
    :type tag: ~azure.mgmt.costmanagement.models.QueryComparisonExpression
    """

    _validation = {
        'and_property': {'min_items': 2},
        'or_property': {'min_items': 2},
    }

    _attribute_map = {
        'and_property': {'key': 'and', 'type': '[QueryFilter]'},
        'or_property': {'key': 'or', 'type': '[QueryFilter]'},
        'not_property': {'key': 'not', 'type': 'QueryFilter'},
        'dimension': {'key': 'dimension', 'type': 'QueryComparisonExpression'},
        'tag': {'key': 'tag', 'type': 'QueryComparisonExpression'},
    }

    def __init__(self, *, and_property=None, or_property=None, not_property=None, dimension=None, tag=None, **kwargs) -> None:
        super(QueryFilter, self).__init__(**kwargs)
        self.and_property = and_property
        self.or_property = or_property
        self.not_property = not_property
        self.dimension = dimension
        self.tag = tag
