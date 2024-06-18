"""This file defines the schemas for the provider and requirer sides of this relation interface.

It must expose two interfaces.schema_base.DataBagSchema subclasses called:
- ProviderSchema
- RequirerSchema
"""

from interface_tester.schema_base import DataBagSchema
from pydantic import BaseModel, AnyHttpUrl, Field
import typing


class ProviderUnitData(BaseModel):
    secret_id: str = Field(
        description="Secret ID for the key you need in order to query this unit.",
        title="Query key secret ID",
        examples=["secret:12312323112313123213"],
    )


class ProviderAppData(BaseModel):
    api_endpoint: AnyHttpUrl = Field(
        description="URL to the database's endpoint.",
        title="Endpoint API address",
        examples=["https://example.com/v1/query"],
    )


class ProviderSchema(DataBagSchema):
    app: ProviderAppData
    unit: ProviderUnitData


class RequirerAppData(BaseModel):
    tables: typing.List[str] = Field(
        description="Tables that the requirer application needs.",
        title="Requested tables.",
        examples=[["users", "passwords"]],
    )


class RequirerSchema(DataBagSchema):
    app: RequirerAppData
    # we can omit `unit` because the requirer makes no use of the unit databags
