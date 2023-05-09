import abc
from typing import Optional, Sequence, Tuple
import numpy as np
import logging

logger = logging.getLogger(__name__)


class Geometry(abc.ABC):
    """ A three-dimensional shape. Geometry objects should be attached to
    Nodes to have a coordinate system in the scene graph. This is an 
    abstract base class which defined the methods subclasses with a 
    concrete geometry should implement.
    """
    def __init__(self,stratTime=0,color=1):
        self._startTime=stratTime
        self._x_Location = -10
        self._y_Location = 0
        self._z_Location = 2
        self._color = color
        # self._isLen = isLen



    @property
    @abc.abstractmethod
    def collision(self):
        """ Return true if the sensor in a len."""
        pass

    @collision.setter
    @abc.abstractmethod
    def collision(self, new_value):
        """ Sets isLen.  """
        pass

    # @property
    @abc.abstractmethod
    def isLen(self):
        """ Return true if the sensor in a len."""
        pass

    # @isLen.setter
    # @abc.abstractmethod
    # def isLen(self, new_value):
    #     """ Sets isLen.  """
    #     pass

    @property
    @abc.abstractmethod
    def material(self):
        """ Return the material attached to this node.
        """
        pass

    @material.setter
    @abc.abstractmethod
    def material(self, new_value):
        """ Sets the material.
        """
        pass

    @abc.abstractmethod
    def is_on_surface(self, point: tuple) -> bool:
        """Returns `True` is the point is on the surface."""
        pass

    @abc.abstractmethod
    def contains(self, point: tuple) -> bool:
        """ Return True if the point is inside the shape.
        """
        pass

    @abc.abstractmethod
    def intersections(self, position: tuple, direction: tuple) -> Sequence[tuple]:
        """Returns tuple of intersection points sorted by distance from origin.
        """
        pass

    @abc.abstractmethod
    def normal(self, surface_point: tuple) -> tuple:
        """ Returns the unit surface normal at the surface_point. Normal faces outwards
            by convention.
        """
        pass

    @abc.abstractmethod
    def is_entering(self, surface_point: tuple, direction: tuple) -> bool:
        """ Returns the unit surface normal at the surface_point.
        """
        pass
