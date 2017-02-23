TEMPL_VHD = """--==============================================================================
-- $long_entity_name
--==============================================================================
--
-- author: $name ($mail)
--
-- date of creation: $date
--
-- version: 1.0
--
-- description:
--
-- dependencies:
--
-- references:
--
--==============================================================================
-- GNU LESSER GENERAL PUBLIC LICENSE
--==============================================================================
-- This source file is free software; you can redistribute it and/or modify it
-- under the terms of the GNU Lesser General Public License as published by the
-- Free Software Foundation; either version 2.1 of the License, or (at your
-- option) any later version. This source is distributed in the hope that it
-- will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
-- of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
-- See the GNU Lesser General Public License for more details. You should have
-- received a copy of the GNU Lesser General Public License along with this
-- source; if not, download it from http://www.gnu.org/licenses/lgpl-2.1.html
--==============================================================================
-- last changes:
--    $date   $name     File created
--==============================================================================
-- TODO: -
--==============================================================================

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity $entity is
end entity $entity;


architecture $arch of $entity is

  --============================================================================
  -- Type declarations
  --============================================================================

  --============================================================================
  -- Constant declarations
  --============================================================================

  --============================================================================
  -- Component declarations
  --============================================================================

  --============================================================================
  -- Signal declarations
  --============================================================================


--==============================================================================
--  architecture begin
--==============================================================================
begin

  --============================================================================
  -- I/O logic
  --============================================================================


end architecture $arch;
--==============================================================================
--  architecture end
--==============================================================================
"""

TEMPL_CHDR = """/*
 *==============================================================================
 * $ftype file for $long_entity_name
 *==============================================================================
 *
 * author: $name ($mail)
 *
 * date of creation: $date
 *
 * version: 1.0
 *
 * description:
 *
 * dependencies:
 *
 * references:
 *
 *==============================================================================
 * GNU LESSER GENERAL PUBLIC LICENSE
 *==============================================================================
 * This source file is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by the
 * Free Software Foundation; either version 2.1 of the License, or (at your
 * option) any later version. This source is distributed in the hope that it
 * will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
 * of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Lesser General Public License for more details. You should have
 * received a copy of the GNU Lesser General Public License along with this
 * source; if not, download it from http://www.gnu.org/licenses/lgpl-2.1.html
 *==============================================================================
 * last changes:
 *    $date   $name     File created
 *==============================================================================
 * TODO: -
 *==============================================================================
 */

#ifndef __${entity}_H_
#define __${entity}_H_

/*
 *==============================================================================
 * <your func name here>
 *
 *  params:
 *     * <your func params here>
 *
 *  returns:
 *    - <your func returns here>
 *
 *  comments:
 *     <your comments here>
 *==============================================================================
 */

#endif // __${entity}_H_
"""

TEMPL_CSRC = """/*
 *==============================================================================
 * $ftype file for $long_entity_name
 *==============================================================================
 *
 * author: $name ($mail)
 *
 * date of creation: $date
 *
 * version: 1.0
 *
 * description:
 *
 * dependencies:
 *
 * references:
 *
 *==============================================================================
 * GNU LESSER GENERAL PUBLIC LICENSE
 *==============================================================================
 * This source file is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by the
 * Free Software Foundation; either version 2.1 of the License, or (at your
 * option) any later version. This source is distributed in the hope that it
 * will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
 * of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Lesser General Public License for more details. You should have
 * received a copy of the GNU Lesser General Public License along with this
 * source; if not, download it from http://www.gnu.org/licenses/lgpl-2.1.html
 *==============================================================================
 * last changes:
 *    $date   $name     File created
 *==============================================================================
 * TODO: -
 *==============================================================================
 */

/*
 *==============================================================================
 * <your func name here>
 *
 *  params:
 *     * <your func params here>
 *
 *  returns:
 *    - <your func returns here>
 *
 *  comments:
 *     <your comments here>
 *==============================================================================
 */
"""

TEMPL_PY = """#===============================================================================
# $long_entity_name
#===============================================================================
# author: $name ($mail)
#
# date of creation: $date
#
# version: 1.0
#
# description:
#
# dependencies:
#
# references:
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
# last changes:
#    $date    $name     File created
#===============================================================================
#  TODO: -
#===============================================================================


#===============================================================================
# <your func name here>
#
#   params:
#     * <your func params here>
#
#   returns:
#     * <your func returns here>
#
#   comments:
#     <your comments here>
#===============================================================================
"""
