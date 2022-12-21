#! /usr/bin/env python
#===============================================================================
# TG -- Template Generator
#===============================================================================
# author: Theodor Stana (theodor.stana@gmail.com)
#
# date of creation: 2013-10-24
#
# version: 1.3
#
# description:
#   TG can be used to generate source files for various programming languages.
#   It is a command-line tool, that asks for the user's input for his name,
#   e-mail address and the name of the file, and based on a template file
#   (tg_templ.py) it generates the source file according to the tempalte.
#
#   The template can be edited by the user according to preference. The reader
#   should use the template variables defined in the documentation when
#   customizing the template file.
#
#   Additionally, an initialization file (tg_ini.py) provides the possibility
#   of defining default values for the $name and $mail template variables. If
#   the user leaves these fields blank when prompted for them, TG uses the
#   defaults defined in the INI file.
#
# dependencies:
#   Various Python stdlib modules, as can be seen below.
#
#===============================================================================
# GNU LESSER GENERAL PUBLIC LICENSE
#===============================================================================
# This source file is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation; either version 2.1 of the License, or (at your
# option) any later version. This source is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details. You should have
# received a copy of the GNU Lesser General Public License along with this
# source; if not, download it from http://www.gnu.org/licenses/lgpl-2.1.html
#===============================================================================

from string import Template
from time import strftime, gmtime
import os

from tg_templ import *

try:
  from tg_ini import *
except ImportError:
  INI_NAME = ""
  INI_MAIL = ""


OPT_CSRC = 2
OPT_CHDR = 3

# makeini function -- not used for the moment
def makeini():
  path = ''
  while not os.path.exists(path):
    print('No specified path to template files exists!')
    path = input('Please specify a path (relative or absolute) to your templates: ')

  if not path.endswith(os.pathsep):
    path += os.sep

  fini = open('tg.ini','w')
  fini.write(path)
  fini.close()

#===============================================================================
# makevhd()
#
#   params:
#     * none.
#
#   returns:
#     * none; a source file is generated in the folder where TG is called from.
#
#   comments:
#
# This function generates a VHDL source (.vhd) file.
#
# The TEMPL_VHD constant in the tg_templ.py file is read to get a string template
# to work on. The current date is retrieved using the stdlib gmtime() function
# and is stored in a variable in the format YYYY-MM-DD.
#
# Then the user is asked to input several details from the command line. These
# are then substituted in the string template and the appropriate file is
# generated.
#===============================================================================
def makevhd():

  # Create a string object based on the template
  vhd  = Template(TEMPL_VHD)

  # Get the current GMT in the format YYYY-MM-DD
  date = strftime("%Y-%m-%d", gmtime())
  year = str(gmtime().tm_year)

  # Prompt the user for details relevant to the design
  design_name = input('Verbose name of the design? ')

  name = input('Company name (%s): ' % INI_NAME)
  if (name == ""):
    name = INI_NAME

  entity = ""
  while (entity == ""):
    entity = input("Entity name? ")

  arch = input("Architecture name (arch): ")
  if (arch == ""):
    arch = "arch"

  # Create a new dictionary to store the user's details for changing the template
  d = {}

  d['design_name'] = design_name
  d['company'] = name
  d['date']    = date
  d['year']    = year
  d['entity']  = entity
  d['arch']    = arch

  # Substitute the dictionary fields in the template
  hdl = vhd.substitute(d)

  # and write the dictionary to the output file
  foutpname = './' + entity + '.vhd'
  foutp = open(foutpname,'w')
  foutp.write(hdl)
  foutp.close()

  print('New file "' + foutpname[2:] + '" created.')


#===============================================================================
# makec(opt)
#
#   params:
#     * opt - integer indicating the type of C file to create
#
#   returns:
#     * none; a source file is generated in the folder where TG is called from.
#
#   comments:
#
# This function generates a C source (.c) or header (.h) file. The OPT parameter
# to the function selects whether the output is a source or a header file.
#
# The TEMPL_C constant in the tg_templ.py file is read to get a string template
# to work on. The current date is retrieved using the stdlib gmtime() function
# and is stored in a variable in the format YYYY-MM-DD.
#
# Then the user is asked to input several details from the command line. These
# are then substituted in the string template and the appropriate file is
# generated. The following details are requested from the user. The variable
# name in the string template is given for reference, in case the reader wants
# to change the template.
#
# +-------------------+----------------------------------------------------+
# |     Variable      |         Comments                                   |
# +-------------------+----------------------------------------------------+
# | $long_entity_name | The name of the current design                     |
# | $name             | The author's name. If the user supplise none, the  |
# |                   | default supplied in tg_ini.py is used.             |
# | $mail             | The author's e-mail. If the user supplise none,    |
# |                   | the default supplied in tg_ini.py is used.         |
# +-------------------+----------------------------------------------------+
#===============================================================================
def makec(opt):

  # Create a string object based on the template
  if (opt == OPT_CSRC):
    vhd  = Template(TEMPL_CSRC)
  else:
    vhd = Template(TEMPL_CHDR)

  # Get the current GMT time in the format YYYY-MM-DD
  date = strftime("%Y-%m-%d", gmtime())

  # Prompt the user for details relevant to the design
  long_entity_name = input('Verbose name of the design? ')

  name   = input('Your name? (%s) ' % INI_NAME)
  if (name == ""):
    name = INI_NAME

  mail   = input('Your e-mail? (%s) ' % INI_MAIL)
  if (mail == ""):
    mail = INI_MAIL

  # Prompt the user for the filename
  fname = ""
  while (fname == ""):
    fname = input("Filename? ")

  # Create a new dictionary to store the user's details for changing the template
  d = {}

  d['long_entity_name'] = long_entity_name
  d['name'] = name
  d['mail'] = mail
  d['date'] = date

  # Split the name into the design name and the extension
  (fnm, fext) = os.path.splitext(fname)

  # Write the type of the C file (header/source) to the file header. The
  # extension of the file is appended to the filename the user inputs. In case
  # the user has given an incorrect filename, it is corrected here.
  if (opt == OPT_CSRC):
    d['ftype'] = 'Source'
    if (fext != '.c'):
      fname = fnm + '.c'
  else:
    d['ftype'] = 'Header'
    if (fext != '.h'):
      fname = fnm + '.h'

  d['entity'] = fnm.upper()

  # Substitute the dictionary fields in the template
  s = vhd.substitute(d)

  # and write the dictionary to the output file
  foutpname = './' + fname

  foutp = open(foutpname,'w')
  foutp.write(s)
  foutp.close()

  print('New file "' + foutpname[2:] + '" created.')

#===============================================================================
# makepy()
#
#   params:
#     * none
#
#   returns:
#     * none; a source file is generated in the folder where TG is called from.
#
#   comments:
#
# A recursive little bastard of a function: Python creating Python. Before we
# get too phylosophical about it, the function simply takes the TEMPL_PY string
# and copies it to a Template object. As the other functions, a dictionary is
# created and predefined variables are substituted in the template string.
#
# The current date is retrieved using the stdlib gmtime() function
# and is stored in a variable in the format YYYY-MM-DD.
#
# Then the user is asked to input several details from the command line. These
# are then substituted in the string template and the appropriate file is
# generated. The following details are requested from the user. The variable
# name in the string template is given for reference, in case the reader wants
# to change the template.
#
# +-------------------+----------------------------------------------------+
# |     Variable      |         Comments                                   |
# +-------------------+----------------------------------------------------+
# | $long_entity_name | The name of the current design                     |
# | $name             | The author's name. If the user supplise none, the  |
# |                   | default supplied in tg_ini.py is used.             |
# | $mail             | The author's e-mail. If the user supplise none,    |
# |                   | the default supplied in tg_ini.py is used.         |
# +-------------------+----------------------------------------------------+
#===============================================================================
def makepy():
  # Create a string object based on the template
  vhd  = Template(TEMPL_PY)

  # Get the current GMT time in the format YYYY-MM-DD
  date = strftime("%Y-%m-%d", gmtime())

  # Prompt the user for details relevant to the design
  long_entity_name = input('Verbose name of the design? ')

  name   = input('Your name? (%s) ' % INI_NAME)
  if (name == ""):
    name = INI_NAME

  mail   = input('Your e-mail? (%s) ' % INI_MAIL)
  if (mail == ""):
    mail = INI_MAIL

  # Prompt the user for the filename
  fname = ""
  while (fname == ""):
    fname = input("Filename? ")

  # Create a new dictionary to store the user's details for changing the template
  d = {}

  d['long_entity_name'] = long_entity_name
  d['name'] = name
  d['mail'] = mail
  d['date'] = date

  # Split the name into the design name and the extension
  (fnm, fext) = os.path.splitext(fname)

  # Appended the file extension to the filename the user inputs, in case it has
  # not been provided, or the one given by the user is incorrect.
  if (fext != '.py'):
    fname = fnm + '.py'

  # Substitute the dictionary fields in the template
  s = vhd.substitute(d)

  # and write the dictionary to the output file
  foutpname = './' + fname

  foutp = open(foutpname,'w')
  foutp.write(s)
  foutp.close()

  print('New file "' + foutpname[2:] + '" created.')

#===============================================================================
# "Main function"
#
#  Presents a user with a command-line menu to select the type of file they want
#  to generate. The file is then generated using one of the local functions.
#===============================================================================
if __name__ == "__main__":

  opt = 10

  # Ask the user for which type of file he/she wants to generate. The menu
  # persists if a wrong option is given.
  while (opt > 4):
    opt = int(input("""Enter:

  (1) for VHDL source
  (2) for C source
  (3) for C header
  (4) for Python source
  (0) to quit

Your option: """));

  # and create the appropriate type of file
  if (opt == 0):
    pass
  elif (opt == 1):
    makevhd()
  elif (opt == 4):
    makepy()
  else:
    makec(opt)

