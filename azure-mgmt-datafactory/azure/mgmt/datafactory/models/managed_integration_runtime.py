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

from .integration_runtime import IntegrationRuntime


class ManagedIntegrationRuntime(IntegrationRuntime):
    """Managed integration runtime, including managed elastic and managed
    dedicated integration runtimes.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Integration runtime description.
    :type description: str
    :param type: Required. Constant filled by server.
    :type type: str
    :ivar state: Integration runtime state, only valid for managed dedicated
     integration runtime. Possible values include: 'Initial', 'Stopped',
     'Started', 'Starting', 'Stopping', 'NeedRegistration', 'Online',
     'Limited', 'Offline', 'AccessDenied'
    :vartype state: str or
     ~azure.mgmt.datafactory.models.IntegrationRuntimeState
    :param compute_properties: The compute resource for managed integration
     runtime.
    :type compute_properties:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeComputeProperties
    :param ssis_properties: SSIS properties for managed integration runtime.
    :type ssis_properties:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeSsisProperties
    """

    _validation = {
        'type': {'required': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'compute_properties': {'key': 'typeProperties.computeProperties', 'type': 'IntegrationRuntimeComputeProperties'},
        'ssis_properties': {'key': 'typeProperties.ssisProperties', 'type': 'IntegrationRuntimeSsisProperties'},
    }

    def __init__(self, **kwargs):
        super(ManagedIntegrationRuntime, self).__init__(**kwargs)
        self.state = None
        self.compute_properties = kwargs.get('compute_properties', None)
        self.ssis_properties = kwargs.get('ssis_properties', None)
        self.type = 'Managed'
