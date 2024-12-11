import json
import jsonschema

json_path = 'ex_1.json'
schema_path = 'schema.json'
error_path = 'error_ex_1.json'

with open(json_path) as good_file, open(schema_path) as sch, open(error_path) as er:
    data_json = json.load(good_file)
    data_schema = json.load(sch)
    data_error = json.load(er)

    try:
        jsonschema.validate(data_json, data_schema)
        print(f'{json_path} is valid')
    except Exception as e:
        print(f'{json_path} is not valid')
        print(e)

    try:
        jsonschema.validate(data_error, data_schema)
        print(f'{error_path} is valid')
    except Exception as e:
        print(f'{error_path} is not valid')
        print(e)