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
## @file    mApplication/applicationInfoAbs.py @brief [ FILE   ] - Application identification classes.
## @package mApplication.applicationInfoAbs    @brief [ MODULE ] - Application identification classes.


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
import sys
import inspect
import importlib

import mApplication.parentApplicationLib

import mCore.platformLib

import mFileSystem.directoryLib
import mFileSystem.fileLib

import mMecoPackage.packageLib
import mMecoPackage.enumLib

import mQtWidgets.iconLib


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ ABSTRACT CLASS ] - Class provides application information for applications.
class ApplicationInfo(object):
    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC STATIC MEMBERS
    # ------------------------------------------------------------------------------------------------
    #
    ## [ str ] - Name of the application info module (file) that contains information about each
    #  application available in the packages.
    INFO_MODULE_FILE_BASE_NAME = 'applicationInfoLib'

    #
    # ------------------------------------------------------------------------------------------------
    # BUILT-IN METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Constructor.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def __init__(self):

        ## [ mMecoPackage.packageLib.Package ] - Package library.
        self._package = mMecoPackage.packageLib.Package(path=inspect.getfile(self.__class__))

        # INFO

        if not hasattr(self, '_name'):
            ## [ str ] - Name of the application.
            self._name         = ''

        if not hasattr(self, '_versionMajor'):
            ## [ int ] - Major version.
            self._versionMajor = 1

        if not hasattr(self, '_versionMinor'):
            ## [ int ] - Minor version.
            self._versionMinor = 0

        if not hasattr(self, '_versionFix'):
            ## [ int ] - Fix version.
            self._versionFix   = 0


        ## [ str ] - String representation of the version.
        self._versionStr       = ''

        ## [ str ] - Window title.
        self._windowTitle      = ''


        if not hasattr(self, '_isActive'):
            ## [ bool ] - Whether this application is active.
            self._isActive  = True


        if not hasattr(self, '_description'):
            ## [ str ] - Description about the application.
            self._description  = ''

        if not hasattr(self, '_iconFileName'):
            ## [ str ] - Name of the icon file.
            self._iconFileName = None

        if not hasattr(self, '_usePlatformIcon'):
            ## [ str ] - Use platform icon.
            #  Use platform icon instead of N/A icon if no icon is provided
            #  for this application.
            self._usePlatformIcon = False

        if not hasattr(self, '_parentApplications'):
            ## [ list of enum ] - Parent applications which this application designed to work in @see mApplication.parentApplicationLib.Application
            self._parentApplications = [mApplication.parentApplicationLib.Application.kAll]

        if not hasattr(self, '_keywords'):
            ## [ list of str ] - Keywords.
            #  These words would be use to search for the application.
            self._keywords     = []

        if not hasattr(self, '_isGUI'):
            ## [ bool ] - Whether this application is a GUI application.
            self._isGUI        = False

        if not hasattr(self, '_runAsPanelInNuke'):
            ## [ bool ] - Whether to run this application as panel in Nuke if its a GUI application.
            self._runAsPanelInNuke = False


        # DOCUMENTS

        if not hasattr(self, '_documents'):
            ## [ list of dict ] - Documentations, keys of dict instances are: title, url.
            self._documents = []


        # COMMAND

        if not hasattr(self, '_pythonCommand'):
            ## [ str ] - Python command to run the application.
            self._pythonCommand = None


        if not hasattr(self, '_command'):
            ## [ str ] - Terminal command to run the application.
            self._command = None


        # MENU

        ## [ str ] - Full menu path.
        self._fullMenuPath     = ''

        if not hasattr(self, '_menuPath'):
            ## [ str ] - Menu path. Use / as separator to give a complete path.
            self._menuPath            = None

        if not hasattr(self, '_menuSeparatorBefore'):
            ## [ bool ] - Add separator before this menu item.
            self._menuSeparatorBefore = False

        if not hasattr(self, '_menuSeparatorAfter'):
            ## [ bool ] - Add separator after this menu item.
            self._menuSeparatorAfter  = False


        # DEVELOPERS INFO

        if not hasattr(self, '_developers'):
            ## [ list of dict ] - Developers, keys of dict instances are userName, name, email, web.
            self._developers = []


        self._initialize()

    #
    ## @brief String representation.
    #
    #  @exception N/A
    #
    #  @return str - String representation.
    def __str__(self):

        return self.asStr()

    #
    # ------------------------------------------------------------------------------------------------
    # PROTECTED METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief Initialize.
    #
    #  Method initializes `_versionStr`, `_windowTitle` and `_menuPath` members.
    #
    #  @exception N/A
    #
    #  @return None - None.
    def _initialize(self):

        # Build version string
        self._versionStr   = '{}.{}.{}'.format(self._versionMajor, self._versionMinor, self._versionFix);

        # Build window title
        self._windowTitle  = '{} - {}'.format(self._name, self._versionStr)

        # Build menu path
        if self._menuPath:

            menuPath = ['Meco']

            menuPath.extend([x for x in self._menuPath.split('/') if x])

            if self._isGUI:
                menuPath.append('{}...'.format(self._windowTitle))
            else:
                menuPath.append(self._windowTitle)

            self._fullMenuPath = '/'.join(menuPath)

    #
    # ------------------------------------------------------------------------------------------------
    # PROPERTY METHODS
    # ------------------------------------------------------------------------------------------------
    ## @name PROPERTIES

    ## @{
    #
    ## @brief Package class instance used by this class.
    #
    #  @exception N/A
    #
    #  @return mMecoPackage.packageLib.Package - Class instance.
    def package(self):

        return self._package

    #
    ## @brief Name of the application.
    #
    #  @exception N/A
    #
    #  @return str - Name.
    def name(self):

        return self._name

    #
    ## @brief Major version of the application.
    #
    #  @exception N/A
    #
    #  @return int - Value.
    def versionMajor(self):

        return self._versionMajor

    #
    ## @brief Minor version of the application.
    #
    #  @exception N/A
    #
    #  @return int - Value.
    def versionMinor(self):

        return self._versionMinor

    #
    ## @brief Fix version of the application.
    #
    #  @exception N/A
    #
    #  @return int - Value.
    def versionFix(self):

        return self._versionFix

    #
    ## @brief Application version in "major.minor.fix" format.
    #
    #  @exception N/A
    #
    #  @return str - Version.
    def versionStr(self):

        return self._versionStr

    #
    ## @brief Window title of the application.
    #
    #  @exception N/A
    #
    #  @return str - Title.
    def windowTitle(self):

        return self._windowTitle

    #
    ## @brief Whether this application is active.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def isActive(self):

        return self._isActive

    #
    ## @brief Description about the application.
    #
    #  @exception N/A
    #
    #  @return str - Description.
    def description(self):

        return self._description

    #
    ## @brief Icon file name used by the application.
    #
    #  @exception N/A
    #
    #  @return str - Icon file name.
    def iconFileName(self):

        return self._iconFileName

    #
    ## @brief Use platform icon instead of N/A icon if no icon is provided for this application.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def usePlatformIcon(self):

        return self._usePlatformIcon

    #
    ## @brief Parent applications which this application can run in.
    #
    #  @see mApplication.parentApplicationLib.Application
    #
    #  @exception N/A
    #
    #  @return list of enum - Parent applications.
    def parentApplications(self):

        return self._parentApplications

    #
    ## @brief Keywords to find this application.
    #
    #  @exception N/A
    #
    #  @return list of str - Keywords.
    def keywords(self):

        return self._keywords

    #
    ## @brief Whether this is a GUI application.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def isGUI(self):

        return self._isGUI

    #
    ## @brief Whether to run this application as panel in Nuke if its a GUI application.
    #
    #  @exception N/A
    #
    #  @return bool - Result.
    def runAsPanelInNuke(self):

        return self._runAsPanelInNuke

    #
    ## @brief Documents of the application.
    #
    #  @exception N/A
    #
    #  @return list of dict - Documentations, keys of dict instances are: title, url.
    def documents(self):

        return self._documents

    #
    ## @brief Python command to run the application.
    #
    #  @exception N/A
    #
    #  @return str - Python command.
    def pythonCommand(self):

        return self._pythonCommand

    #
    ## @brief Terminal command to run the application.
    #
    #  @exception N/A
    #
    #  @return str - Command.
    def command(self):

        return self._command

    #
    ## @brief Full menu path of the application if it appears in menus in parent application.
    #
    #  @exception N/A
    #
    #  @return str - Full menu path.
    def fullMenuPath(self):

        return self._fullMenuPath

    #
    ## @brief Menu path of the application if it appears in menus in parent application.
    #
    #  @exception N/A
    #
    #  @return str - Menu path.
    def menuPath(self):

        return self._menuPath

    #
    ## @brief Add separator before this menu item.
    #
    #  @exception N/A
    #
    #  @return bool - Value.
    def menuSeparatorBefore(self):

        return self._menuSeparatorBefore

    #
    ## @brief Add separator after this menu item.
    #
    #  @exception N/A
    #
    #  @return bool - Value.
    def menuSeparatorAfter(self):

        return self._menuSeparatorAfter

    #
    ## @brief Developers worked on this application.
    #
    #  @exception N/A
    #
    #  @return list of dict - Developers, keys of dict instances are `username`, `name`, `email`, `web`.
    def developers(self):

        return self._developers

    #
    ## @}

    #
    # ------------------------------------------------------------------------------------------------
    # PUBLIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief String representation.
    #
    #  @exception N/A
    #
    #  @return str - Information about the application in human readable form.
    def asStr(self):

        info = '\n'
        info += 'Name                : {}\n'.format(self._name)
        info += 'Version             : {}\n'.format(self._versionStr)
        info += 'Description         : {}\n'.format(self._description)
        info += 'Icon File Name      : {}\n'.format(self._iconFileName)

        info += 'Parent Applications : {}\n'.format(self.getParentApplicationsAsStr())
        info += 'Keywords            : {}\n'.format(self.getKeywordsAsStr())

        isGUI = 'True' if self._isGUI else 'False'
        info += 'GUI                 : {}\n'.format(isGUI)

        info += 'Python Command      : {}\n'.format(self._pythonCommand)
        info += 'Command             : {}\n'.format(self._command)

        info += 'Menu Path           : {}\n'.format(self._menuPath)
        info += 'Full Menu Path      : {}\n'.format(self._fullMenuPath)

        info += 'Package Path        : {}\n'.format(self._package.path())

        documents = ''
        if self._documents:
            documents = '\n'
            for d in self._documents:
                documents += '                      {} : {}'.format(d['title'].ljust(15), d['url'])
            documents += '\n'

        if not documents:
            documents = 'N/A\n'

        info += 'Documents           : {}'.format(documents)


        developers = ''
        if self._developers:
            developers = '\n'
            for d in self._developers:
                for i in d:
                    developers += '                      {} : {}\n'.format(i.title().ljust(15), d[i])
                developers += '\n'

        if not developers:
            developers = 'N/A'

        info += 'Developers          : {}'.format(developers)

        return info

    #
    ## @brief Get HTML string representation.
    #
    #  This method provides information so it can be used on a GUI such as about dialog.
    #
    #  @exception N/A
    #
    #  @return str - Information about the application in human readable form in HTML format.
    def asHTML(self):

        info = ''

        info += '<b>Name                 :</b> {}<br><br>'.format(self._name)
        info += '<b>Version              :</b> {}<br><br>'.format(self._versionStr)
        info += '<b>Description          :</b> {}<br><br>'.format(self._description)

        info += '<b>Parent Applications  :</b> {}<br><br>'.format(self.getParentApplicationsAsStr())
        info += '<b>Keywords             :</b> {}<br><br>'.format(self.getKeywordsAsStr())

        isGUI = 'True' if self._isGUI else 'False'
        info += '<b>GUI                  :</b> {}<br><br>'.format(isGUI)

        info += '<b>Python Command       :</b> {}<br><br>'.format(self._pythonCommand)
        info += '<b>Command              :</b> {}<br><br>'.format(self._command)

        info += '<b>Menu Path            :</b> {}<br><br>'.format(self._menuPath)
        info += '<b>Full Menu Path       :</b> {}<br><br>'.format(self._fullMenuPath)

        info += '<b>Path                 :</b> {}<br><br>'.format(self._package.path())

        documents = ''
        if self._documents:
            documents = '<br>'
            for d in self._documents:
                documents += '    <b>{} :</b> {}<br>'.format(d['title'].ljust(15), d['url'])
            documents += '<br>'

        if not documents:
            documents = 'N/A<br>'

        info += '<b>Documents           :</b> <br>{}<br>'.format(documents)


        developers = '<br>'
        if self._developers:
            developers = '<br>'
            for d in self._developers:
                for i in d:
                    developers += '    <b>{} :</b> {}<br>'.format(i.title().ljust(15), d[i])
                developers += '<br>'

        if not developers:
            developers = 'N/A<br>'

        info += '<b>Developers          :</b> <br>{}<br>'.format(developers)


        return info

    #
    ## @brief Get parent applications as a string separated by comma.
    #
    #  An empty string returns if no parent application is set.
    #
    #  @exception N/A
    #
    #  @return str - Parent applications.
    def getParentApplicationsAsStr(self):

        if not self._parentApplications:
            return ''

        return ', '.join(self._parentApplications)

    #
    ## @brief Get keywords as a string separated by comma.
    #
    #  An empty string returns if no keyword is set.
    #
    #  @exception N/A
    #
    #  @return str - Keywords.
    def getKeywordsAsStr(self):

        if not self._keywords:
            return ''

        return ', '.join(self._keywords)

    #
    ## @brief Get developer user names as a string separated by comma.
    #
    #  An empty string returns if no developers is set.
    #
    #  @exception N/A
    #
    #  @return str - Developer user names.
    def getDeveloperUserNamesAsStr(self):

        if not self._developers:
            return ''

        developers = []

        for d in self._developers:
            developers.append(d['userName'])

        return ', '.join(developers)

    #
    ## @brief Get developer email addresses as a string separated by comma.
    #
    #  An empty string returns if no developers is set.
    #
    #  @exception N/A
    #
    #  @return str - Developer email addresses.
    def getDeveloperEmailAddressesAsStr(self):

        if not self._developers:
            return ''

        emails = []

        for d in self._developers:
            emails.append(d['email'])

        return ', '.join(emails)

    #
    ## @brief Get icon file absolute path used by this application.
    #
    #  @exception N/A
    #
    #  @return str - Absolute path of the icon file.
    def getIconFileAbsolutePath(self):

        _iconLib = mQtWidgets.iconLib.Icon(inspect.getfile(self.__class__))

        if not self._iconFileName:

            if not self._usePlatformIcon:
                return _iconLib.getFile(self._iconFileName, useNA=True)
            else:
                platformIcon = mQtWidgets.iconLib.PlatformIcon.getValueFromAttributeName(mCore.platformLib.Platform.system(),
                                                                                         removeK=True)
                return _iconLib.getFile(platformIcon)

        return _iconLib.getFile(self._iconFileName, useNA=True)

    #
    ## @brief Get QIcon instance for the icon file used by this application.
    #
    #  @exception N/A
    #
    #  @return QIcon - QIcon instance.
    def getIcon(self):

        _iconLib = mQtWidgets.iconLib.Icon(inspect.getfile(self.__class__))

        if not self._iconFileName:

            if not self._usePlatformIcon:
                return _iconLib.createIcon(self._iconFileName, useNA=True)
            else:
                platformIcon = mQtWidgets.iconLib.PlatformIcon.getValueFromAttributeName(mCore.platformLib.Platform.system(),
                                                                                         removeK=True)
                return _iconLib.createIcon(platformIcon)

        return _iconLib.createIcon(self._iconFileName, useNA=True)

    #
    ## @brief Get QPixmap instance for the icon file used by this application.
    #
    #  @exception N/A
    #
    #  @return QPixmap - QPixmap instance.
    def getPixmap(self):

        _iconLib = mQtWidgets.iconLib.Icon(inspect.getfile(self.__class__))

        if not self._iconFileName:

            if not self._usePlatformIcon:
                return _iconLib.createPixmap(self._iconFileName, useNA=True)
            else:
                platformIcon = mQtWidgets.iconLib.PlatformIcon.getValueFromAttributeName(mCore.platformLib.Platform.system(),
                                                                                         removeK=True)
                return _iconLib.createPixmap(platformIcon)

        return _iconLib.createPixmap(self._iconFileName, useNA=True)

    #
    # ------------------------------------------------------------------------------------------------
    # STATIC METHODS
    # ------------------------------------------------------------------------------------------------
    #
    ## @brief List all application info classes (applications) available in the packages.
    #
    #  @param parentApplication [ str  | None | in  ] - Parent application name, which listed applications can be run in.
    #  @param packageName       [ str  | None | in  ] - Name of the package, the applications will be list for.
    #  @param keyword           [ str  | None | in  ] - Keyword to be searched.
    #  @param ignoreInactive    [ bool | True | in  ] - Ignore, therefore do not list inactive applications.
    #
    #  @exception N/A
    #
    #  @return list of mApplication.applicationInfoAbs.ApplicationInfo - List of application info class instances.
    @staticmethod
    def list(parentApplication=None, packageName=None, keyword=None, ignoreInactive=True):

        appInfoList = []

        _package    = mMecoPackage.packageLib.Package()
        _dir        = mFileSystem.directoryLib.Directory()
        _moduleDir  = mFileSystem.directoryLib.Directory()
        _file       = mFileSystem.fileLib.File()

        for path in sys.path:

            if not _dir.setDirectory(directory=path):
                continue

            directoryList = _dir.listDirectories()
            if not directoryList:
                continue

            for directory in directoryList:

                if not _moduleDir.setDirectory(directory):
                    continue

                if not _package.setPackage(directory):
                    continue

                if packageName:
                    if packageName.lower() != _package.name().lower():
                        continue

                fileList = _moduleDir.listFilesWithAbsolutePath(extension='py')
                if not fileList:
                    continue

                fileList = [x for x in fileList if x.endswith('{}.py'.format(mMecoPackage.enumLib.PackagePythonFileSuffix.kApp))]

                if not fileList:
                    continue

                for appInfoFile in fileList:

                    if not _file.setFile(appInfoFile):
                        continue

                    _module = importlib.import_module('{}.{}'.format(_moduleDir.getBaseName(), _file.baseName()))

                    for name, obj in inspect.getmembers(_module):

                        if not inspect.isclass(obj):
                            continue

                        _appInfo = obj()

                        if ignoreInactive and not _appInfo.isActive():
                            continue

                        if parentApplication and parentApplication != mApplication.parentApplicationLib.Application.kAll:
                            if parentApplication not in _appInfo.parentApplications():
                                del _appInfo
                                continue

                        if keyword:
                            if not keyword in _appInfo.keywords() and not keyword in _appInfo.name().lower():
                                continue

                        appInfoList.append(_appInfo)

        if appInfoList:
            appInfoList.sort(key=lambda x: x.name())

        return appInfoList
