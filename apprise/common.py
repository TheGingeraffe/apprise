# -*- coding: utf-8 -*-
#
# Base Notify Wrapper
#
# Copyright (C) 2017 Chris Caron <lead2gold@gmail.com>
#
# This file is part of apprise.
#
# apprise is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# apprise is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with apprise. If not, see <http://www.gnu.org/licenses/>.


class NotifyType(object):
    """
    A simple mapping of notification types most commonly used with
    all types of logging and notification services.
    """
    INFO = 'info'
    SUCCESS = 'success'
    FAILURE = 'failure'
    WARNING = 'warning'


NOTIFY_TYPES = (
    NotifyType.INFO,
    NotifyType.SUCCESS,
    NotifyType.FAILURE,
    NotifyType.WARNING,
)


class NotifyImageSize(object):
    """
    A list of pre-defined image sizes to make it easier to work with defined
    plugins.
    """
    XY_72 = '72x72'
    XY_128 = '128x128'
    XY_256 = '256x256'


NOTIFY_IMAGE_SIZES = (
    NotifyImageSize.XY_72,
    NotifyImageSize.XY_128,
    NotifyImageSize.XY_256,
)