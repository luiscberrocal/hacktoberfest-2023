from __future__ import annotations

from pydantic import BaseModel, Field


class Location(BaseModel):
    latitude: str
    longitude: str
    human_address: str


class Incident(BaseModel):
    unique_key: str
    created_date: str
    agency: str
    agency_name: str
    complaint_type: str
    descriptor: str
    location_type: str
    incident_zip: str
    incident_address: str
    street_name: str
    cross_street_1: str
    cross_street_2: str
    address_type: str
    city: str
    status: str
    resolution_description: str
    resolution_action_updated_date: str
    community_board: str
    bbl: str
    borough: str
    x_coordinate_state_plane: str
    y_coordinate_state_plane: str
    open_data_channel_type: str
    park_facility_name: str
    park_borough: str
    latitude: str
    longitude: str
    location: Location
    __computed_region_efsh_h5xi: str = Field(..., alias=':@computed_region_efsh_h5xi')
    __computed_region_f5dn_yrer: str = Field(..., alias=':@computed_region_f5dn_yrer')
    __computed_region_yeji_bk3q: str = Field(..., alias=':@computed_region_yeji_bk3q')
    __computed_region_92fq_4b7q: str = Field(..., alias=':@computed_region_92fq_4b7q')
    __computed_region_sbqj_enih: str = Field(..., alias=':@computed_region_sbqj_enih')
