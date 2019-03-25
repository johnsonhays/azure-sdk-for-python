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


class AcceptTransferRequest(Model):
    """Request parameters to accept transfer.

    :param product_details: Request parameters to accept transfer.
    :type product_details: list[~azure.mgmt.billing.models.ProductDetails]
    """

    _attribute_map = {
        'product_details': {'key': 'properties.productDetails', 'type': '[ProductDetails]'},
    }

    def __init__(self, **kwargs):
        super(AcceptTransferRequest, self).__init__(**kwargs)
        self.product_details = kwargs.get('product_details', None)
