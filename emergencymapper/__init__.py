# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EmergencyMapper
                                 A QGIS plugin
 This plugin is to compute the Emergency features such as buildings and population data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-06-05
        copyright            : (C) 2018 by Geoinformatics Center, Asian Institute of Technology
        email                : ashokdahal@ait.asia
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load EmergencyMapper class from file EmergencyMapper.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Emergency_Mapper import EmergencyMapper
    return EmergencyMapper(iface)