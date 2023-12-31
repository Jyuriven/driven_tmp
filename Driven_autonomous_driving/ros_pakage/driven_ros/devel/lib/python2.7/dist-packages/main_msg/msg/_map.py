# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from main_msg/map.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class map(genpy.Message):
  _md5sum = "97eb6427ffcca94f25feb3e4b16337f3"
  _type = "main_msg/map"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int16[] x_lst
int16[] y_lst
int16 car_x
int16 car_y"""
  __slots__ = ['x_lst','y_lst','car_x','car_y']
  _slot_types = ['int16[]','int16[]','int16','int16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x_lst,y_lst,car_x,car_y

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(map, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.x_lst is None:
        self.x_lst = []
      if self.y_lst is None:
        self.y_lst = []
      if self.car_x is None:
        self.car_x = 0
      if self.car_y is None:
        self.car_y = 0
    else:
      self.x_lst = []
      self.y_lst = []
      self.car_x = 0
      self.car_y = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.x_lst)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(struct.Struct(pattern).pack(*self.x_lst))
      length = len(self.y_lst)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(struct.Struct(pattern).pack(*self.y_lst))
      _x = self
      buff.write(_get_struct_2h().pack(_x.car_x, _x.car_y))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.x_lst = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.y_lst = s.unpack(str[start:end])
      _x = self
      start = end
      end += 4
      (_x.car_x, _x.car_y,) = _get_struct_2h().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.x_lst)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(self.x_lst.tostring())
      length = len(self.y_lst)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(self.y_lst.tostring())
      _x = self
      buff.write(_get_struct_2h().pack(_x.car_x, _x.car_y))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.x_lst = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.y_lst = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
      _x = self
      start = end
      end += 4
      (_x.car_x, _x.car_y,) = _get_struct_2h().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2h = None
def _get_struct_2h():
    global _struct_2h
    if _struct_2h is None:
        _struct_2h = struct.Struct("<2h")
    return _struct_2h
