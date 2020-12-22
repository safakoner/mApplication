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
## @file    mApplication/parentApplicationLib.py @brief [ FILE   ] - Parent applications.
## @package mApplication.parentApplicationLib    @brief [ MODULE ] - Parent applications.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import mCore.enumAbs


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ ENUM CLASS ] - Application list.
class Application(mCore.enumAbs.Enum):

    ## [ str ] - All applications.
    kAll        = 'all'

    ## [ str ] - Houdini.
    kHoudini    = 'houdini'

    ## [ str ] - Katana.
    kKatana     = 'katana'

    ## [ str ] - Mari.
    kMari       = 'mari'

    ## [ str ] - Maya.
    kMaya       = 'maya'

    ## [ str ] - Nuke.
    kNuke       = 'nuke'

    ## [ str ] - Photoshop.
    kPhotoshop  = 'photoshop'

    ## [ str ] - Standalone.
    kStandalone = 'standalone'

    ## [ str ] - ZBrush.
    kZBrush     = 'zbrush'

    #
    # ------------------------------------------------------------------------------------------------
    # OVERWRITTEN CLASS METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief List static public attributes of the class.
    #
    #  @param cls                 [ object | None  | in  ] - Class object.
    #  @param stringOnly          [ bool   | True  | in  ] - List attributes only with string values.
    #  @param getValues           [ bool   | True  | in  ] - Get values of the attributes instead of their names.
    #  @param removeK             [ bool   | True  | in  ] - Remove k character from the attribute names if getValues is provided False.
    #  @param startAttrNamesLower [ bool   | False | in  ] - Start attribute names with lower case.
    #
    #  @exception N/A
    #
    #  @return list of str - Names or values of the attributes.
    @classmethod
    def listAttributes(cls, stringOnly=True, getValues=True, removeK=True, startAttrNamesLower=False):

        ignoreList = [cls.kStandalone, cls.kAll]
        
        data = []
        
        for attr, value in cls.__dict__.items():

            if attr.startswith('__'):
                continue

            if getValues:

                if stringOnly:
                    if isinstance(value, str):
                        data.append(value)
                else:
                    data.append(value)

            else:

                if removeK and attr.startswith('k'):
                    attr = attr[1:]

                if startAttrNamesLower:
                    attr = '{}{}'.format(attr[:1].lower(), attr[1:])

                data.append(attr)
        
        data = [x for x in data if not x in ignoreList]

        data.sort()

        return data
    
    #
    ## @brief Get current parent application if any.
    #  
    #  @exception N/A
    #  
    #  @return str - Name of the parent application from mApplication.parentApplication.Application enum class.
    @staticmethod
    def getCurrent():
        
        import mApplication.importLib

        return mApplication.importLib.PARENT_APPLICATION

#
## @brief [ ENUM CLASS ] - Applications used by developers.
class DeveloperApplication(mCore.enumAbs.Enum):
    
    ## [ str ] - Doxygen.
    kDoxygen    = 'doxygen'
    
    ## [ str ] - Wing IDE.
    kWingIDE    = 'wingide'
    
    ## [ str ] - PyCharm.
    kPyCharm    = 'pycharm'

