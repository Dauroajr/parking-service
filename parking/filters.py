from dj_rql.filter_cls import AutoRQLFilterClass

from .models import ParkingSpot, ParkingRecords


class ParkingSpotFilterClass(AutoRQLFilterClass):

    MODEL = ParkingSpot


class ParkingRecordsFilterClass(AutoRQLFilterClass):

    MODEL = ParkingRecords
    FILTERS = (
        {
            "filter": "license_plate",
            "source": "vehicle__license_plate",
        },
    )
