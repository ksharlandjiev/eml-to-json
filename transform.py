import glob
import datetime
import json
import eml_parser
import os
import base64

def json_serial(obj):
  if isinstance(obj, datetime.datetime):
      serial = obj.isoformat()
      return serial

def json_save(filename, obj):
  filename = "./json/"+filename+".json"
  
  f = open(filename, "a")
  f.write(obj)
  f.close()
  
ep = eml_parser.EmlParser()

for filepath in glob.iglob('eml/*.eml'):
    # print(filepath)
    raw_email = None
    with open(filepath, 'rb') as fhdl:
      raw_email = fhdl.read()

    parsed_eml = ep.decode_email_bytes(raw_email)
    os.path.splitext(os.path.basename(filepath))[0]
    json_file = os.path.splitext(os.path.basename(filepath))[0]
    # print (parsed_eml)
    json_save(json_file, json.dumps(parsed_eml, default=json_serial))

  #   f = open("demofile2.txt", "a")
  # f.write("Now the file has more content!")
  # f.close()
  #   print(json.dumps(parsed_eml, default=json_serial))

