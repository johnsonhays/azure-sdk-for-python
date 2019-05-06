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

from enum import Enum


class TimeframeType(str, Enum):

    week_to_date = "WeekToDate"
    month_to_date = "MonthToDate"
    year_to_date = "YearToDate"
    the_last_week = "TheLastWeek"
    the_last_month = "TheLastMonth"
    the_last_year = "TheLastYear"
    custom = "Custom"
    billing_month_to_date = "BillingMonthToDate"
    the_last_billing_month = "TheLastBillingMonth"


class GranularityType(str, Enum):

    daily = "Daily"
    hourly = "Hourly"


class QueryColumnType(str, Enum):

    tag = "Tag"
    dimension = "Dimension"


class SortDirection(str, Enum):

    ascending = "Ascending"
    descending = "Descending"


class StatusType(str, Enum):

    active = "Active"
    inactive = "Inactive"


class RecurrenceType(str, Enum):

    daily = "Daily"
    weekly = "Weekly"
    monthly = "Monthly"
    annually = "Annually"


class FormatType(str, Enum):

    csv = "Csv"


class ExecutionType(str, Enum):

    on_demand = "OnDemand"
    scheduled = "Scheduled"


class ExecutionStatus(str, Enum):

    queued = "Queued"
    in_progress = "InProgress"
    completed = "Completed"
    failed = "Failed"
    timeout = "Timeout"
    new_data_not_available = "NewDataNotAvailable"
    data_not_available = "DataNotAvailable"
