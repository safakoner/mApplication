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
## @file    mApplication/applicationCmd.py @brief [ FILE   ] - Command module.
## @package mApplication.applicationCmd    @brief [ MODULE ] - Command module.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import os
import argparse
import json

import mApplication.applicationInfoAbs

import mCore.displayLib

import mMecoSettings.envVariablesLib


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief List applications.
#
#  @exception N/A
#
#  @return None - None.
def listApplications():

    parser = argparse.ArgumentParser(description='List applications')

    parser.add_argument('-d',
                        '--detail',
                        action='store_true',
                        help='Display details about the applications')

    parser.add_argument('-li',
                        '--list-inactive',
                        action='store_true',
                        help='List inactive applications')

    parser.add_argument('-pa',
                        '--parent-application',
                        type=str,
                        default='',
                        help='Parent application name, which listed applications can be run in',
                        required=False)

    parser.add_argument('-p',
                        '--package',
                        type=str,
                        default='',
                        help='Name of the package, the applications will be listed for',
                        required=False)

    parser.add_argument('-k',
                        '--keyword',
                        type=str,
                        default='',
                        help='Keyword, which will be used to find applications with',
                        required=False)

    _args = parser.parse_args()

    displayAppFilterSuggestion()

    detail            = _args.detail
    parentApplication = _args.parent_application
    packageName       = _args.package
    keyword           = _args.keyword
    listInactive      = not _args.list_inactive

    applicationList = mApplication.applicationInfoAbs.ApplicationInfo.list(parentApplication=parentApplication,
                                                                           packageName=packageName,
                                                                           keyword=keyword,
                                                                           ignoreInactive=listInactive)
    if not applicationList:
        mCore.displayLib.Display.displayInfo('No application found.')
        return

    mCore.displayLib.Display.displayBlankLine()

    for application in  applicationList:

        if detail:
            mCore.displayLib.Display.displayInfo(application, startNewLine=False)
        else:
            mCore.displayLib.Display.displayInfo('{}{}{}'.format(application.name().ljust(50),
                                                                 application.versionStr().ljust(10),
                                                                 application.getParentApplicationsAsStr()),
                                                 endNewLine=False)

    if not detail:
        mCore.displayLib.Display.displayBlankLine()

    mCore.displayLib.Display.displayInfo(('\n{} application(s) listed.\n'.format(len(applicationList))))

#
## @brief Search applications.
#
#  @exception N/A
#
#  @return None - None.
def search():

    parser = argparse.ArgumentParser(description='Search applications')

    parser.add_argument('keyword',
                        type=str,
                        help='Keyword to be searched')

    parser.add_argument('-d',
                        '--detail',
                        action='store_true',
                        help='Display details about the applications')

    parser.add_argument('-li',
                        '--list-inactive',
                        action='store_true',
                        help='List inactive applications')

    parser.add_argument('-pa',
                        '--parent-application',
                        type=str,
                        default='',
                        help='Parent application name, which listed applications can be run in',
                        required=False)

    parser.add_argument('-p',
                        '--package',
                        type=str,
                        default='',
                        help='Name of the package, the applications will be listed for',
                        required=False)

    _args = parser.parse_args()

    displayAppFilterSuggestion()

    keyword           = _args.keyword.lower()
    detail            = _args.detail
    parentApplication = _args.parent_application
    packageName       = _args.package
    listInactive      = not _args.list_inactive

    applicationList = mApplication.applicationInfoAbs.ApplicationInfo.list(parentApplication=parentApplication,
                                                                           packageName=packageName,
                                                                           keyword=keyword,
                                                                           ignoreInactive=listInactive)
    if not applicationList:
        mCore.displayLib.Display.displayBlankLine()
        mCore.displayLib.Display.displayInfo('No application found.\n')
        return

    applicationCount = 0

    mCore.displayLib.Display.displayBlankLine()

    for application in  applicationList:

        applicationCount += 1

        if detail:
            mCore.displayLib.Display.displayInfo(application, startNewLine=False)
        else:
            mCore.displayLib.Display.displayInfo('{}{}{}'.format(application.name().ljust(50),
                                                                 application.versionStr().ljust(10),
                                                                 application.getParentApplicationsAsStr()),
                                                 endNewLine=False)

    if not detail:
        mCore.displayLib.Display.displayBlankLine()

    if applicationCount:
        mCore.displayLib.Display.displayInfo('\n{} application(s) listed.\n'.format(applicationCount))
    else:
        mCore.displayLib.Display.displayInfo('No application found.\n')

#
## @brief Display app filter suggestion.
#
#  @exception N/A
#
#  @return None - None.
def displayAppFilterSuggestion():

    appPath = os.environ.get(mMecoSettings.envVariablesLib.MECO_APP_PATH, None)
    if not appPath:
        return

    if not os.path.isfile(appPath):
        return

    _file = open(appPath, 'r')
    appData = json.loads(_file.read())
    _file.close()

    if 'application' in appData:

        message = 'You can also use "-pa {}" in order to filter applications for the parent application, which this '\
                  'environment is initialized for.'.format(appData['application'])

        mCore.displayLib.Display.displayInfo(message, endNewLine=False)
