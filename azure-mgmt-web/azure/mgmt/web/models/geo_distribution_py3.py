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


class GeoDistribution(Model):
    """A global distribution definition.

    :param location: Location.
    :type location: str
    :param number_of_workers: NumberOfWorkers.
    :type number_of_workers: int
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'number_of_workers': {'key': 'numberOfWorkers', 'type': 'int'},
    }

    def __init__(self, *, location: str=None, number_of_workers: int=None, **kwargs) -> None:
        super(GeoDistribution, self).__init__(**kwargs)
        self.location = location
        self.number_of_workers = number_of_workers
