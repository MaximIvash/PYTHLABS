import xmlschema

xml_file = 'ex_1.xml'
xml_error_file = 'error.xml'
xsd_file = 'schema.xsd'

with open(xsd_file) as f:
    schema = xmlschema.XMLSchema(f)
    print(f"валидация файла {xml_file} по созданной схеме -", schema.is_valid(xml_file))
    print(f"валидация файла {xml_error_file} по созданной схеме -", schema.is_valid(xml_error_file))