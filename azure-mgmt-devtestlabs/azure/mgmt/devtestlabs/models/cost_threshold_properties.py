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


class CostThresholdProperties(Model):
    """Properties of a cost threshold item.

    :param threshold_id: The ID of the cost threshold item.
    :type threshold_id: str
    :param percentage_threshold: The value of the percentage cost threshold.
    :type percentage_threshold:
     ~azure.mgmt.devtestlabs.models.PercentageCostThresholdProperties
    :param display_on_chart: Indicates whether this threshold will be
     displayed on cost charts. Possible values include: 'Enabled', 'Disabled'
    :type display_on_chart: str or
     ~azure.mgmt.devtestlabs.models.CostThresholdStatus
    :param send_notification_when_exceeded: Indicates whether notifications
     will be sent when this threshold is exceeded. Possible values include:
     'Enabled', 'Disabled'
    :type send_notification_when_exceeded: str or
     ~azure.mgmt.devtestlabs.models.CostThresholdStatus
    :param notification_sent: Indicates the datetime when notifications were
     last sent for this threshold.
    :type notification_sent: str
    """

    _attribute_map = {
        'threshold_id': {'key': 'thresholdId', 'type': 'str'},
        'percentage_threshold': {'key': 'percentageThreshold', 'type': 'PercentageCostThresholdProperties'},
        'display_on_chart': {'key': 'displayOnChart', 'type': 'str'},
        'send_notification_when_exceeded': {'key': 'sendNotificationWhenExceeded', 'type': 'str'},
        'notification_sent': {'key': 'notificationSent', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CostThresholdProperties, self).__init__(**kwargs)
        self.threshold_id = kwargs.get('threshold_id', None)
        self.percentage_threshold = kwargs.get('percentage_threshold', None)
        self.display_on_chart = kwargs.get('display_on_chart', None)
        self.send_notification_when_exceeded = kwargs.get('send_notification_when_exceeded', None)
        self.notification_sent = kwargs.get('notification_sent', None)
