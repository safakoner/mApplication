#
# Copyright 2020 Safak Oner.
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------
## @file    mApplication/importLib.py @brief [ FILE   ] - Import module for applications.
## @package mApplication.importLib    @brief [ MODULE ] - Import module for applications.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import mApplication.parentApplicationLib


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
## [ str ] - Current parent application, available applications are listed in mApplication.applicationLib.Application enum class.
PARENT_APPLICATION = mApplication.parentApplicationLib.Application.kStandalone

# Houdini
try:
    import hou
    PARENT_APPLICATION = mApplication.parentApplicationLib.Application.kHoudini
except ImportError:
    pass

# Katana
try:
    import Katana
    PARENT_APPLICATION = mApplication.parentApplicationLib.Application.kKatana
except ImportError:
    pass

# Mari
try:
    import mari
    PARENT_APPLICATION = mApplication.parentApplicationLib.Application.kMari
except ImportError:
    pass

# Maya
try:
    from maya import cmds
    PARENT_APPLICATION = mApplication.parentApplicationLib.Application.kMaya
except ImportError:
    pass

# Nuke
try:
    import nuke
    PARENT_APPLICATION = mApplication.parentApplicationLib.Application.kNuke
except ImportError:
    pass




