TEMPL_VHD = """--==============================================================================
-- $long_entity_name
--==============================================================================
--
-- author: $name ($mail)
--
-- date of creation: $date
--
-- description:
--
--      <TODO: Add description...>
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

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity $entity is
end entity $entity;


architecture $arch of $entity is

  --============================================================================
  -- Functions
  --============================================================================
  -- log2
  function log2_ceil(N : natural) return positive is
  begin
    if N <= 2 then
      return 1;
    elsif N mod 2 = 0 then
      return 1 + log2_ceil(N/2);
    else
      return 1 + log2_ceil((N+1)/2);
    end if;
  end;

  --============================================================================
  -- Types
  --============================================================================

  --============================================================================
  -- Constants
  --============================================================================

  --============================================================================
  -- Components
  --============================================================================

  --============================================================================
  -- Signals
  --============================================================================


begin -- $arch

  --============================================================================
  -- I/O logic
  --============================================================================


end architecture $arch;
"""

TEMPL_CHDR = """/*
 *==============================================================================
 * $long_entity_name
 *
 * $ftype file
 *==============================================================================
 *
 * author: $name ($mail)
 *
 * date of creation: $date
 *
 * description:
 *
 *      TODO: Add description here...
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
 * $long_entity_name
 *
 * $ftype file
 *==============================================================================
 *
 * author: $name ($mail)
 *
 * date of creation: $date
 *
 * description:
 *
 *      TODO: Add description here...
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
# description:
#
#       TODO: Add description here...
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
