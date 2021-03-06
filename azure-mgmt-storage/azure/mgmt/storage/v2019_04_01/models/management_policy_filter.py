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


class ManagementPolicyFilter(Model):
    """Filters limit rule actions to a subset of blobs within the storage account.
    If multiple filters are defined, a logical AND is performed on all filters.
    .

    All required parameters must be populated in order to send to Azure.

    :param prefix_match: An array of strings for prefixes to be match.
    :type prefix_match: list[str]
    :param blob_types: Required. An array of predefined enum values. Only
     blockBlob is supported.
    :type blob_types: list[str]
    """

    _validation = {
        'blob_types': {'required': True},
    }

    _attribute_map = {
        'prefix_match': {'key': 'prefixMatch', 'type': '[str]'},
        'blob_types': {'key': 'blobTypes', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ManagementPolicyFilter, self).__init__(**kwargs)
        self.prefix_match = kwargs.get('prefix_match', None)
        self.blob_types = kwargs.get('blob_types', None)
