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


class GatewayRoute(Model):
    """GatewayRoute.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar local_address: The gateway's local address
    :vartype local_address: str
    :ivar network: The route's network prefix
    :vartype network: str
    :ivar next_hop: The route's next hop
    :vartype next_hop: str
    :ivar source_peer: The peer this route was learned from
    :vartype source_peer: str
    :ivar origin: The source this route was learned from
    :vartype origin: str
    :ivar as_path: The route's AS path sequence
    :vartype as_path: str
    :ivar weight: The route's weight
    :vartype weight: int
    """

    _validation = {
        'local_address': {'readonly': True},
        'network': {'readonly': True},
        'next_hop': {'readonly': True},
        'source_peer': {'readonly': True},
        'origin': {'readonly': True},
        'as_path': {'readonly': True},
        'weight': {'readonly': True},
    }

    _attribute_map = {
        'local_address': {'key': 'localAddress', 'type': 'str'},
        'network': {'key': 'network', 'type': 'str'},
        'next_hop': {'key': 'nextHop', 'type': 'str'},
        'source_peer': {'key': 'sourcePeer', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'as_path': {'key': 'asPath', 'type': 'str'},
        'weight': {'key': 'weight', 'type': 'int'},
    }

    def __init__(self):
        self.local_address = None
        self.network = None
        self.next_hop = None
        self.source_peer = None
        self.origin = None
        self.as_path = None
        self.weight = None
