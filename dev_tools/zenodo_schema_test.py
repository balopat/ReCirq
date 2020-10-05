import json
import ssl
from urllib.request import urlopen

import jsonschema
import pytest


def test_zenodo_config():
    ignore_ssl = ssl.SSLContext()
    schema_url = ('https://zenodo.org/schemas/records/record-v1.0.0.json')
    with urlopen(schema_url, context=ignore_ssl) as f_schema:
        schema = json.load(f_schema)
        with open(".zenodo.json", "rb") as f_config:
            config = json.load(f_config)
            try:
                jsonschema.validate(config, schema)
            except jsonschema.exceptions.ValidationError as e:
                pytest.fail(e.message)
