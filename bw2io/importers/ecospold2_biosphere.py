from ..units import normalize_units
from .base import ImportBase
from ..strategies import drop_unspecified_subcategories
from bw2data.utils import recursive_str_to_unicode
from lxml import objectify
import os

EMISSIONS_CATEGORIES = {
    "air":   "emission",
    "soil":  "emission",
    "water": "emission",
}


class Ecospold2BiosphereImporter(ImportBase):
    strategies = [drop_unspecified_subcategories]
    db_name = u'biosphere3'
    format = u'Ecoinvent XML'

    def __init__(self):
        self.data = self.extract()

    def extract(self):
        def extract_flow_data(o):
            ds = {
                'categories': (
                    o.compartment.compartment.text,
                    o.compartment.subcompartment.text
                ),
                'code': o.get('id'),
                'name': o.name.text,
                'database': 'biosphere3',
                'exchanges': [],
                'unit': normalize_units(o.unitName.text),
            }
            ds[u"type"] = EMISSIONS_CATEGORIES.get(
                ds['categories'][0], ds['categories'][0]
            )
            return ds

        fp = os.path.join(
            os.path.dirname(__file__),
            "..", "data", "lci",
            "ecoinvent elementary flows 3.1.xml"
        )
        root = objectify.parse(open(fp)).getroot()
        return recursive_str_to_unicode([extract_flow_data(ds)
                                         for ds in root.iterchildren()])