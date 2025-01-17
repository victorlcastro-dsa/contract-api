from .base_schema import BaseRequestSchema, BaseResponseSchema
from datetime import date
from typing import Optional

class GeneralInformationRequestSchema(BaseRequestSchema):
    contract_id: int
    supervision: bool = False
    supervision_frequency: Optional[str] = None
    supervision_description: Optional[str] = None
    technical_reports: bool = False
    technical_reports_frequency: Optional[str] = None
    billing_documents: Optional[str] = None
    client_documents: Optional[str] = None
    pre_start_date: Optional[date] = None
    start_date: Optional[date] = None
    monthly_date: Optional[date] = None
    quarterly_date: Optional[date] = None
    biannual_date: Optional[date] = None
    yearly_date: Optional[date] = None
    near_office: bool = False
    office_city: Optional[str] = None
    contractual_guarantee: bool = False
    guarantee_percentage: Optional[float] = None

class GeneralInformationResponseSchema(BaseResponseSchema):
    contract_id: int
    supervision: bool = False
    supervision_frequency: Optional[str] = None
    supervision_description: Optional[str] = None
    technical_reports: bool = False
    technical_reports_frequency: Optional[str] = None
    billing_documents: Optional[str] = None
    client_documents: Optional[str] = None
    pre_start_date: Optional[date] = None
    start_date: Optional[date] = None
    monthly_date: Optional[date] = None
    quarterly_date: Optional[date] = None
    biannual_date: Optional[date] = None
    yearly_date: Optional[date] = None
    near_office: bool = False
    office_city: Optional[str] = None
    contractual_guarantee: bool = False
    guarantee_percentage: Optional[float] = None