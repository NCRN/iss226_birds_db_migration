"""
Hard code the crosswalk for each destination table.

A crosswalk is a dataframe that documents where `destination` data come from in the `source` data.
Downstream in this pipeline (`src.make_templates._execute_xwalks()`), the program reads the crosswalk and executes the information stored there.

Crosswalks divide `destination` fields into three types and assign values to three columns for each field:
1. 1:1 fields. The destination field has a matching source field.
    a. `source` captures the source field name
    b. `calculation` is 'map_source_to_destination_1_to_1'.
    c. `note` is usually np.NaN
2. Calculated fields. The destination field is calculated from one or more source fields.
    a. `source` captures the python code to generate the `destination` field.
    b. `calculation` is 'calculate_dest_field_from_source_field'.
    c. `note` is a plain-english explanation of the code in `source`.
3. Blanks. The destination field does not fit into the first two categories and is not required; it has no matching source field and cannot be calculated from source fields.
    These are usually fields NCRN doesn't collect.
    a. `source` is np.NaN.
    b. `calculation` is 'blank_field'.
    c. `note` is 'this field was not collected by NCRN and has no NCRN equivalent'.

"""

import pandas as pd
import numpy as np
import src.db_connect as dbc
import datetime

def _ncrn_DetectionEvent(xwalk_dict:dict) -> dict:
    """Make the crosswalk for source.tbl_Events to destination.ncrn.DetectionEvent

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """
    
    # 1:1 fields
    one_to_one_fields = [
        'ID'
        ,'LocationID'
        ,'ProtocolID'
        ,'EnteredBy'
        ,'AirTemperature'
        ,'Notes'
        ,'EnteredDateTime'
        ,'DataProcessingLevelID'
        ,'DataProcessingLevelDate'
        ,'RelativeHumidity'
        ,'SamplingMethodID'
        ,'Observer_ContactID'
        ,'Recorder_ContactID'
        ,'ProtocolNoiseLevelID'
        ,'ProtocolWindCodeID'
        ,'ProtocolPrecipitationTypeID'
        ,'Observer_ExperienceLevelID'
        ,'StartDateTime'
    ]
    # assign grouping variable `calculation` for the 1:1 fields
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'].isin(one_to_one_fields))
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['calculation'] =  np.where(mask, 'map_source_to_destination_1_to_1', xwalk_dict['ncrn.DetectionEvent']['xwalk']['calculation'])
    # ID
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'ID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'event_id', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # LocationID
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'LocationID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'location_id', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # ProtocolID
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'ProtocolID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'protocol_id', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # EnteredBy
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'EnteredBy')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'entered_by', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # AirTemperature
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'AirTemperature')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'temperature', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # Notes
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'Notes')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'event_notes', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # EnteredDateTime
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'EnteredDateTime')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'entered_date', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['note'] =  np.where(mask, 'ncrn.entered_date is collected as a date, not a datetime, so the entered time is unknown', xwalk_dict['ncrn.DetectionEvent']['xwalk']['note'])
    # DataProcessingLevelID
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'DataProcessingLevelID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'dataprocessinglevelid', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # DataProcessingLevelDate
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'DataProcessingLevelDate')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'dataprocessingleveldate', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # RelativeHumidity
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'RelativeHumidity')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'humidity', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # `SamplingMethodID`
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'SamplingMethodID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'protocol_name', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # `Observer_ContactID`
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'Observer_ContactID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'observer', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # `Recorder_ContactID`
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'Recorder_ContactID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'recorder', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # `ProtocolNoiseLevelID`: [lu.NoiseLevel]([ID]) # does NCRN capture an equivalent to this?
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'ProtocolNoiseLevelID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'protocol_id', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # `ProtocolWindCodeID`: [lu.WindCode]([ID]) # does NCRN capture an equivalent to this?
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'ProtocolWindCodeID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'protocol_id', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # `ProtocolPrecipitationTypeID`: [lu.PrecipitationType]([ID]) # does NCRN capture an equivalent to this?
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'ProtocolPrecipitationTypeID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'protocol_id', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # `Observer_ExperienceLevelID`: [lu.ExperienceLevel]([ID])
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'Observer_ExperienceLevelID')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'Position_Title', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # `StartDateTime`
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'StartDateTime')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'activity_start_datetime', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['note'] =  np.where(mask, "a concatenation of tbl_Events.Date and tbl_Events.start_time", xwalk_dict['ncrn.DetectionEvent']['xwalk']['note'])

    # Calculated fields
    calculated_fields = [
        'AirTemperatureRecorded'
        ,'IsSampled'
        ,'TemperatureUnitCode'
        ,'ExcludeNote'
        ,'ExcludeEvent'
    ]
    # mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'].isin(calculated_fields)) # TODO: DELETE THIS LINE, FOR TESTING ONLY# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO
    # xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] = np.where(mask, 'placeholder', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source']) # TODO: DELETE THIS LINE, FOR TESTING ONLY# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO
    # assign grouping variable `calculation` for the calculated fields
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'].isin(calculated_fields))
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['calculation'] =  np.where(mask, 'calculate_dest_field_from_source_field', xwalk_dict['ncrn.DetectionEvent']['xwalk']['calculation'])
    # `AirTemperatureRecorded` BIT type (bool as 0 or 1); not a NCRN field. Should be 1 when the row has a value in `AirTemperature`
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'AirTemperatureRecorded')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] = np.where(mask, "xwalk_dict['ncrn.DetectionEvent']['tbl_load']['AirTemperatureRecorded']=np.where((xwalk_dict['ncrn.DetectionEvent']['tbl_load'].AirTemperature.isna()), 0, 1)", xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # `IsSampled` BIT type (bool as 0 or 1) I think this is the inverse of src_tbl.is_excluded, which is a boolean in Access with one unique value: [0]
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'IsSampled')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, "xwalk_dict['ncrn.DetectionEvent']['tbl_load']['IsSampled'] = np.where((xwalk_dict['ncrn.DetectionEvent']['source']['flaggroup'].isna()), 1, 0)", xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['note'] =  np.where(mask, "BIT type (bool as 0 or 1) correlates to ncrn.tbl_Events.flaggroup, which is a pick-list that defaults to NA. NA indicates a sample was collected.", xwalk_dict['ncrn.DetectionEvent']['xwalk']['note'])
    # `TemperatureUnitCode`: [lu.TemperatureUnit]([ID]) # does NCRN capture an equivalent to this?
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'TemperatureUnitCode')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, "xwalk_dict['ncrn.DetectionEvent']['tbl_load']['TemperatureUnitCode'] = 1", xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['note'] =  np.where(mask, "temperature collected in celsius", xwalk_dict['ncrn.DetectionEvent']['xwalk']['note'])
    # ExcludeNote
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'ExcludeNote')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, "xwalk_dict['ncrn.DetectionEvent']['tbl_load']['ExcludeNote']=xwalk_dict['ncrn.DetectionEvent']['source']['flaggroup']+': '+xwalk_dict['ncrn.DetectionEvent']['source']['label']", xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    # `ExcludeEvent`: this is a 1 or 0 depending on `ExcludeNote`
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'] == 'ExcludeEvent')
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, "xwalk_dict['ncrn.DetectionEvent']['tbl_load']['ExcludeEvent'] = np.where((xwalk_dict['ncrn.DetectionEvent']['source']['label'].isna()), 0, 1)", xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])

    # Blanks
    blank_fields = [
        'DataProcessingLevelNote'
        ,'Rowversion'
        ,'UserCode'
    ]
    # assign grouping variable `calculation` for the blank fields
    mask = (xwalk_dict['ncrn.DetectionEvent']['xwalk']['destination'].isin(blank_fields))
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['calculation'] =  np.where(mask, 'blank_field', xwalk_dict['ncrn.DetectionEvent']['xwalk']['calculation'])
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'] =  np.where(mask, 'blank_field', xwalk_dict['ncrn.DetectionEvent']['xwalk']['source'])
    xwalk_dict['ncrn.DetectionEvent']['xwalk']['note'] =  np.where(mask, 'this field was not collected by NCRN and has no NCRN equivalent', xwalk_dict['ncrn.DetectionEvent']['xwalk']['note'])

    return xwalk_dict

def _ncrn_BirdDetection(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tbl_Event to destination.ncrn.BirdDetection

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """
    # xwalk_dict['ncrn.BirdDetection']['source_name'] = 'tbl_Field_Data'
    # xwalk_dict['ncrn.DetectionEvent']['xwalk']

        # 1:1 fields
    one_to_one_fields = [
        'ID'
        ,'DetectionEventID'
        ,'SexID'
        ,'ProtocolDistanceClassID'
        ,'ProtocolTimeIntervalID'
        ,'BirdSpeciesParkID'
        ,'ProtocolDetectionTypeID'
        ,'ExcludeReason'
    ]
    # assign grouping variable `calculation` for the 1:1 fields
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'].isin(one_to_one_fields))
    xwalk_dict['ncrn.BirdDetection']['xwalk']['calculation'] =  np.where(mask, 'map_source_to_destination_1_to_1', xwalk_dict['ncrn.BirdDetection']['xwalk']['calculation'])
    # ID
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'ID')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] =  np.where(mask, 'Data_ID', xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    # DetectionEventID
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'DetectionEventID')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] =  np.where(mask, 'Event_ID', xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    # SexID
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'SexID')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] =  np.where(mask, 'Sex_ID', xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    # ProtocolDistanceClassID
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'ProtocolDistanceClassID')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] =  np.where(mask, 'Distance_id', xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    # ProtocolTimeIntervalID
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'ProtocolTimeIntervalID')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] =  np.where(mask, 'Interval', xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    # BirdSpeciesParkID
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'BirdSpeciesParkID')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] =  np.where(mask, 'AOU_Code', xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    # ProtocolDetectionTypeID
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'ProtocolDetectionTypeID')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] =  np.where(mask, 'ID_Method_Code', xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    # ExcludeReason
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'ExcludeReason')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] =  np.where(mask, 'FlagDescription', xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])

    calculated_fields = [
        'ExcludeDetection'
        ,'NumberIndividuals'
        ,'DetectionNotes'
        ,'ImportNotes'
    ]
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'].isin(calculated_fields)) # TODO: DELETE THIS LINE, FOR TESTING ONLY# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] = np.where(mask, 'placeholder', xwalk_dict['ncrn.BirdDetection']['xwalk']['source']) # TODO: DELETE THIS LINE, FOR TESTING ONLY# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO# TODO
    # assign grouping variable `calculation` for the calculated fields
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'].isin(calculated_fields))
    xwalk_dict['ncrn.BirdDetection']['xwalk']['calculation'] =  np.where(mask, 'calculate_dest_field_from_source_field', xwalk_dict['ncrn.BirdDetection']['xwalk']['calculation'])
    # ExcludeDetection  BIT type (bool as 0 or 1); should be 0 when `DataFlag` == False
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'ExcludeDetection')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] = np.where(mask, "xwalk_dict['ncrn.BirdDetection']['tbl_load']['ExcludeDetection']=np.where((xwalk_dict['ncrn.BirdDetection']['source']['DataFlag']==False), 0, 1)", xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    xwalk_dict['ncrn.BirdDetection']['xwalk']['note'] = np.where(mask, "BIT type (bool as 0 or 1); should be 0 when `DataFlag` == False", xwalk_dict['ncrn.BirdDetection']['xwalk']['note'])
    # NumberIndividuals  NCRN recorded bird detections as one-row-per-individual in tbl_Field_Data
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'NumberIndividuals')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] = np.where(mask, "xwalk_dict['ncrn.BirdDetection']['tbl_load']['NumberIndividuals']=1", xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    xwalk_dict['ncrn.BirdDetection']['xwalk']['note'] = np.where(mask, "NCRN recorded bird detections as one-row-per-individual in tbl_Field_Data", xwalk_dict['ncrn.BirdDetection']['xwalk']['note'])
    # DetectionNotes  NCRN recorded bird detections as one-row-per-individual in tbl_Field_Data
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'DetectionNotes')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] = np.where(mask, "xwalk_dict['ncrn.BirdDetection']['tbl_load']['DetectionNotes']='Previously_Obs: ' + xwalk_dict['ncrn.BirdDetection']['source']['Previously_Obs'].astype(str)", xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    xwalk_dict['ncrn.BirdDetection']['xwalk']['note'] = np.where(mask, "NCRN's access db has a field `tbl_Field_Data.Previously_Obs` which has no equivalent in sql server. Recording this field as a note to preserve data short-term. Long-term solution is feature-request to add field ncrn.BirdDetection.Previously_Obs", xwalk_dict['ncrn.BirdDetection']['xwalk']['note'])
    # ImportNotes  NCRN recorded bird detections as one-row-per-individual in tbl_Field_Data
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'] == 'ImportNotes')
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] = np.where(mask, "xwalk_dict['ncrn.BirdDetection']['tbl_load']['ImportNotes']='Initial_Three_Min_Cnt: ' + xwalk_dict['ncrn.BirdDetection']['source']['Initial_Three_Min_Cnt'].astype(str)", xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    xwalk_dict['ncrn.BirdDetection']['xwalk']['note'] = np.where(mask, "NCRN's access db has a field `tbl_Field_Data.Initial_Three_Min_Cnt` which has no equivalent in sql server. Recording this field as a note to preserve data short-term. Long-term solution is feature-request to add field ncrn.BirdDetection.Initial_Three_Min_Cnt", xwalk_dict['ncrn.BirdDetection']['xwalk']['note'])

    # Blanks
    blank_fields = [
        'DataProcessingLevelNote'
        ,'Rowversion'
        ,'UserCode'
    ]
    # assign grouping variable `calculation` for the blank fields
    mask = (xwalk_dict['ncrn.BirdDetection']['xwalk']['destination'].isin(blank_fields))
    xwalk_dict['ncrn.BirdDetection']['xwalk']['calculation'] =  np.where(mask, 'blank_field', xwalk_dict['ncrn.BirdDetection']['xwalk']['calculation'])
    xwalk_dict['ncrn.BirdDetection']['xwalk']['source'] =  np.where(mask, 'blank_field', xwalk_dict['ncrn.BirdDetection']['xwalk']['source'])
    xwalk_dict['ncrn.BirdDetection']['xwalk']['note'] =  np.where(mask, 'this field was not collected by NCRN and has no NCRN equivalent', xwalk_dict['ncrn.BirdDetection']['xwalk']['note'])

    return xwalk_dict

def _ncrn_Protocol(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tbl_Protocol to destination.ncrn.Protocol

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _ncrn_Location(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tbl_Locations to destination.ncrn.Location

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    # do we really collect data from >4k sites?!

    return xwalk_dict

def _ncrn_Park(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_Park_Code to destination.ncrn.Park

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _lu_TimeInterval(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_interval to destination.lu.TimeInterval

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _lu_WindCode(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_Wind_Code to destination.lu.WindCode

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict


def _lu_DataProcessingLevel(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.DataProcessingLevel to destination.lu.DataProcessingLevel

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _lu_DetectionType(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_Bird_ID_Method to destination.lu.DetectionType

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _lu_DistanceClass(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.dbo_tlu_Distance_Estimate to destination.lu.DistanceClass

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _lu_GeodeticDatum(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_Datum to destination.lu.GeodeticDatum

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _lu_Sex(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_Sex_Code to destination.lu.Sex

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _ncrn_Contact(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_Contacts to destination.ncrn.Contact

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    # use tlu_Contacts.Position_Title as experience level
    # if tlu_Contacts.Position_Title as experience level

    return xwalk_dict

def _lu_PrecipitationType(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_Sky_Code to destination.lu.PrecipitationType

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _ncrn_BirdSpeciesPark(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_Species to destination.ncrn.BirdSpeciesPark

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """
    # ncrn.BirdSpeciesPark is a park-level grouping variable for species in ncrn.BirdGroups
    # NCRN doesn't maintain attributes like this so it's probably a blank table

    return xwalk_dict

def _ncrn_BirdSpeciesGroup(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_Species to destination.ncrn.BirdSpeciesPark

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """
    # ncrn.BirdSpeciesGroups is a species-level grouping variable for species in ncrn.BirdGroups
    # NCRN doesn't maintain this

    # TODO: Fill this table with the attributes from tlu_Species (i.e., the grouping variables)
    # e.g., tlu_Species.Target_Species_Forest
    # e.g., tlu_Species.Target_Species_Grassland
    # e.g., tlu_Species.Target_Species_Grassland

    return xwalk_dict

def _ncrn_BirdGroups(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.dbo_tlu_Guild_Assignment to destination.ncrn.BirdGroups

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    # ncrn.BirdGroups
    # looks like dbo_tlu_Guild_Assignment LEFT JOIN dbo_tbl_Guilds?
    # dbo_tlu_Guild_Assignment.Guild_Assignment_ID == dbo.ncrn.BirdGroups.ID --I know this GUID needs to be translated to INT
    # dbo_tlu_GuildAssignment.Guild_Level == dbo.ncrn.BirdGroups.GroupName
    # dbo.ncrn.BirdGroups.GroupName = 1 --BIT; all of our groups are guilds
    # dbo_tlu_GuildAssignment.Active == dbo.ncrn.BirdGroups.IsActive
    # dbo_tbl_Guilds.Integrity_Element + dbo_tbl_Guilds.Guild_Name == dbo.ncrn.BirdGroups.Comment

    return xwalk_dict

def _lu_NoiseLevel(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tlu_Disturbance to destination.lu.NoiseLevel

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict


def _ncrn_AuditLog(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tbl_History to destination.ncrn.AuditLog

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _ncrn_AuditLogDetail(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tbl_History to destination.ncrn.AuditLogDetail

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict

def _lu_SamplingMethod(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tbl_Protocol to destination.lu.SamplingMethod

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """

    return xwalk_dict


def _lu_Habitat(xwalk_dict:dict) -> dict: ##TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO####TODO##TODO##TODO##
    """Crosswalk source.tbl_Protocol to destination.lu.Habitat

    Args:
        xwalk_dict (dict): dictionary of column names crosswalked between source and destination tables

    Returns:
        dict: dictionary of column names crosswalked between source and destination tables with data updated for this table
    """
    # in the app, "habitat" seems to be a 1:many attribute of a sampling location
    # NCRN hasn't historically subdivided beyond "Forest" and "Grassland" so we just use tbl_Protocol 

    return xwalk_dict


def _exception_ncrn_DetectionEvent(xwalk_dict:dict) -> dict:
    """Exceptions associated with the generation of destination table ncrn.DetectionEvent"""

    #  EXCEPTION 1: exceptions from storing observers/recorders in long-format instead of wide-format
    con = dbc._db_connect('access')
    with open(r'src\qry\qry_long_event_contacts.sql', 'r') as query:
        df = pd.read_sql_query(query.read(),con)
    con.close()

    mysorts = df.groupby(['Event_ID']).size().reset_index(name='count').sort_values(['count'], ascending=True)
    double_events = mysorts[mysorts['count']>1].Event_ID.unique()
    single_events = mysorts[mysorts['count']==1].Event_ID.unique()
    zero_events = mysorts[mysorts['count']==0].Event_ID.unique()
    # len(df) == len(singles) + len(doubles) # sanity check

    # edge case: >1 person was associated with the event
    mask = (df['Event_ID'].isin(double_events)) & (df['Contact_Role']!='Observer')
    df['Contact_Role'] = np.where(mask, 'Recorder', df['Contact_Role'])
    mask = (df['Event_ID'].isin(double_events))
    lookup = df[mask].copy()
    lookup['observer'] = lookup['Contact_ID']
    lookup['recorder'] = lookup['Contact_ID']
    lookup = lookup.drop_duplicates('Event_ID').reset_index()[['Event_ID', 'observer', 'recorder']]
    df = df.merge(lookup, on='Event_ID', how='left')

    # edge case: 0 people were associated with the event
    mask = (df['Event_ID'].isin(zero_events))
    df['observer'] = np.where(mask, np.NaN, df['observer'])
    df['recorder'] = np.where(mask, np.NaN, df['recorder'])

    # base case: one-and-only-one person was associated with the event
    mask = (df['Event_ID'].isin(single_events))
    df['observer'] = np.where(mask, df['Contact_ID'], df['observer'])
    df['recorder'] = np.where(mask, df['Contact_ID'], df['recorder'])

    # cleanup
    df = df.drop_duplicates('Event_ID')
    df = df[['Event_ID', 'observer', 'recorder', 'Position_Title']]
    df.rename(columns={'Event_ID':'event_id'}, inplace=True)

    xwalk_dict['ncrn.DetectionEvent']['source'] = xwalk_dict['ncrn.DetectionEvent']['source'].merge(df, on='event_id', how='left')

    # EXCEPTION 2: exceptions from storing date and time separately instead of as datetime
    xwalk_dict['ncrn.DetectionEvent']['source']['Date'] = xwalk_dict['ncrn.DetectionEvent']['source']['Date'].dt.date
    xwalk_dict['ncrn.DetectionEvent']['source']['start_time'] = xwalk_dict['ncrn.DetectionEvent']['source']['start_time'].dt.time
    xwalk_dict['ncrn.DetectionEvent']['source']['start_time'] = np.where((xwalk_dict['ncrn.DetectionEvent']['source']['start_time'].isna()), datetime.time(0, 0),xwalk_dict['ncrn.DetectionEvent']['source']['start_time'] )
    xwalk_dict['ncrn.DetectionEvent']['source']['Date'] = np.where((xwalk_dict['ncrn.DetectionEvent']['source']['Date'].isna()), datetime.date(1900, 1, 1),xwalk_dict['ncrn.DetectionEvent']['source']['Date'] )
    xwalk_dict['ncrn.DetectionEvent']['source'].loc[:,'activity_start_datetime'] = pd.to_datetime(xwalk_dict['ncrn.DetectionEvent']['source'].Date.astype(str)+' '+xwalk_dict['ncrn.DetectionEvent']['source'].start_time.astype(str))

    return xwalk_dict




