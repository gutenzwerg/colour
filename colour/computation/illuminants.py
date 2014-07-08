# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**illuminants.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines **Colour** package *illuminants* relative spectral power distributions computation objects.

**Others:**

"""

from __future__ import unicode_literals

import numpy

import colour.dataset.illuminants.d_illuminants_s_spds
import colour.utilities.exceptions
import colour.utilities.verbose
from colour.computation.spectrum import SpectralPowerDistribution

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["D_illuminant_relative_spd"]

LOGGER = colour.utilities.verbose.install_logger()


def D_illuminant_relative_spd(xy):
    """
    Returns the relative spectral power distribution of given *CIE Standard Illuminant D Series* *xy* chromaticity coordinates.

    References:

    -  http://www.brucelindbloom.com/Eqn_DIlluminant.html, **Wyszecki & Stiles**, *Color Science - Concepts and Methods Data and Formulae - Second Edition*, Page 146.

    Usage::

        >>> D_illuminant_relative_spd((0.34567, 0.35850))
        <colour.computation.SpectralPowerDistribution object at 0x101023590>

    :param xy: *xy* chromaticity coordinate.
    :type xy: tuple
    :return: *CIE Standard Illuminant D Series* relative spectral power distribution.
    :rtype: SpectralPowerDistribution
    """

    M = 0.0241 + 0.2562 * xy[0] - 0.7341 * xy[1]
    M1 = (-1.3515 - 1.7703 * xy[0] + 5.9114 * xy[1]) / M
    M2 = (0.0300 - 31.4424 * xy[0] + 30.0717 * xy[1]) / M

    distribution = {}
    start, end, steps = colour.dataset.illuminants.d_illuminants_s_spds.D_ILLUMINANTS_S_SPDS.get("S0").shape
    for i in numpy.arange(start, end + steps, steps):
        S0 = colour.dataset.illuminants.d_illuminants_s_spds.D_ILLUMINANTS_S_SPDS_DATA.get("S0").get(i)
        S1 = colour.dataset.illuminants.d_illuminants_s_spds.D_ILLUMINANTS_S_SPDS_DATA.get("S1").get(i)
        S2 = colour.dataset.illuminants.d_illuminants_s_spds.D_ILLUMINANTS_S_SPDS_DATA.get("S2").get(i)
        distribution[i] = S0 + M1 * S1 + M2 * S2

    return SpectralPowerDistribution("CIE Standard Illuminant D Series", distribution)