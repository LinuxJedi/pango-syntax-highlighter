# vim:expandtab:shiftwidth=2:tabstop=2:smarttab:
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain 
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import pangopygments
import argparse

parser = argparse.ArgumentParser(description='Syntax highlight code in Pango format')
parser.add_argument ('language', help='the syntax language of the input file')
parser.add_argument('input', type=argparse.FileType('r'), help='the input file')
parser.add_argument('output', type=argparse.FileType('w'), help='the output file')
args= parser.parse_args()

input_data= args.input.read()

output_data= pangopygments.highlight(input_data, args.language)

args.output.write(output_data)

