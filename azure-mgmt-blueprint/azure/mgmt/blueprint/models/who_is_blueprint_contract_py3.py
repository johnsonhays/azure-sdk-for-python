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


class WhoIsBlueprintContract(Model):
    """Response schema for querying the Azure Blueprints service principal in the
    tenant.

    :param object_id: AAD object Id of the Azure Blueprints service principal
     in the tenant.
    :type object_id: str
    """

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
    }

    def __init__(self, *, object_id: str=None, **kwargs) -> None:
        super(WhoIsBlueprintContract, self).__init__(**kwargs)
        self.object_id = object_id
