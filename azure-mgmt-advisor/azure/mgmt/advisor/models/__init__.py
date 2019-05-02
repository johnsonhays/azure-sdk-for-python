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

try:
    from .metadata_supported_value_detail_py3 import MetadataSupportedValueDetail
    from .metadata_entity_py3 import MetadataEntity
    from .config_data_properties_py3 import ConfigDataProperties
    from .config_data_py3 import ConfigData
    from .arm_error_response_body_py3 import ARMErrorResponseBody
    from .short_description_py3 import ShortDescription
    from .resource_recommendation_base_py3 import ResourceRecommendationBase
    from .resource_py3 import Resource
    from .operation_display_info_py3 import OperationDisplayInfo
    from .operation_entity_py3 import OperationEntity
    from .suppression_contract_py3 import SuppressionContract
except (SyntaxError, ImportError):
    from .metadata_supported_value_detail import MetadataSupportedValueDetail
    from .metadata_entity import MetadataEntity
    from .config_data_properties import ConfigDataProperties
    from .config_data import ConfigData
    from .arm_error_response_body import ARMErrorResponseBody
    from .short_description import ShortDescription
    from .resource_recommendation_base import ResourceRecommendationBase
    from .resource import Resource
    from .operation_display_info import OperationDisplayInfo
    from .operation_entity import OperationEntity
    from .suppression_contract import SuppressionContract
from .metadata_entity_paged import MetadataEntityPaged
from .config_data_paged import ConfigDataPaged
from .resource_recommendation_base_paged import ResourceRecommendationBasePaged
from .operation_entity_paged import OperationEntityPaged
from .suppression_contract_paged import SuppressionContractPaged
from .advisor_management_client_enums import (
    Category,
    Impact,
    Risk,
)

__all__ = [
    'MetadataSupportedValueDetail',
    'MetadataEntity',
    'ConfigDataProperties',
    'ConfigData',
    'ARMErrorResponseBody',
    'ShortDescription',
    'ResourceRecommendationBase',
    'Resource',
    'OperationDisplayInfo',
    'OperationEntity',
    'SuppressionContract',
    'MetadataEntityPaged',
    'ConfigDataPaged',
    'ResourceRecommendationBasePaged',
    'OperationEntityPaged',
    'SuppressionContractPaged',
    'Category',
    'Impact',
    'Risk',
]
