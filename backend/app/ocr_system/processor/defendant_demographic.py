import re
from typing import List, Optional, Dict

from app.schemas.dd_schemas import DefendantDemographicBase

def extract_defendant_demographic(raw_text: str) -> DefendantDemographicBase:
    """
    Takes the raw text from the OCR systems and breaks it down into individual fields
    :param raw_text: Entire text output from the OCR system
    :type raw_text: str
    :return: A base schema representing the formatted data
    :rtype: CriminalComplaintBase
    """

    dates = find_dates(raw_text)
    # the following date variables assume all dates were recorded properly by the scan -- need to fix that assumption
    if 0 < len(dates):
        date_of_birth = dates[0]
    else:
        date_of_birth = None
    # incident report number
    cc_temp = DefendantDemographicBase(DOB=date_of_birth)
    return cc_temp



def find_dates(document) -> Optional[List[str]]:
    dates = re.findall("[0-9]{2}/[0-9]{2}/[0-9]{4}", document)
    if dates is not None:
        return dates
    return None

def find_gender(document) -> Optional[List[str]]:
    gender = re.findall("[0-9]{2}/[0-9]{2}/[0-9]{4}", document)
    if gender is not None:
        return gender
    return None

def find_zip(document) -> Optional[List[str]]:
    zip = re.findall("[0-9]{5}", document)
    if zip is not None:
        return zip
    return None

