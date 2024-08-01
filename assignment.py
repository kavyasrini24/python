def personal_details():
    name = input("enter the name:")
    age = input("enter the age:")
    address = input("enter the address:")
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))


personal_details()


import argparse
import os
import xml.etree.ElementTree as ET
from src.config import read_properties_file, load_xml_files
from src.parser import parse_properties_file
from src.utils import output_mode, log_missing_properties
from src.model import Model
