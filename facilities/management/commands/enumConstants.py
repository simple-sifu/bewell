from enum import IntEnum

#  0 - Facility ID,
#  1 - Facility Name,
#  2 - Short Description,
#  3 - Description,
#  4 - Facility Open Date,
#  5 - Facility Address 1,
#  6 - Facility Address 2,
#  7 - Facility City,
#  8 - Facility State,
#  9 - Facility Zip Code,
# 10 - Facility Phone Number,
# 11 - Facility Fax Number,
# 12 - Facility Website,
# 13 - Facility County Code,
# 14 - Facility County,
# 15 - Regional Office ID,
# 16 - Regional Office,
# 17 - Main Site Name,
# 18 - Main Site Facility ID,
# 19 - Operating Certificate Number,
# 20 - Operator Name,
# 21 - Operator Address 1,
# 22 - Operator Address 2,
# 23 - Operator City,
# 24 - Operator State,
# 25 - Operator Zip Code,
# 26 - Cooperator Name,
# 27 - Cooperator Address,
# 28 - Cooperator Address 2,
# 29 - Cooperator City,
# 30 - Cooperator State,
# 31 - Cooperator Zip Code,
# 32 - Ownership Type,
# 33 - Facility Latitude,
# 34 - Facility Longitude,
# 35 - Facility Location


class HealthFacilityColumns(IntEnum):
    FACILITY_ID = 0
    NAME = 1
    OPEN_DATE = 4


class DescriptionColumns(IntEnum):
    SHORT_DESCRIPTION = 2
    DESCRIPTION = 3


class LocationColumns(IntEnum):
    FACILITY_ADDRESS_1 = 5
    FACILITY_ADDRESS_2 = 6
    FACILITY_CITY = 7
    FACILITY_STATE = 8
    FACILITY_ZIP_CODE = 9
    FACILITY_PHONE_NUMBER = 10
    FACILITY_FAX_NUMBER = 11
    FACILITY_WEBSITE = 12
    FACILITY_COUNTY_CODE = 13
    FACILITY_COUNTY = 14
    FACILITY_LATITUDE = 33
    FACILITY_LONGITUDE = 34
    FACILITY_LOCATION = 35
