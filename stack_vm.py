import dis

dis.dis(lambda x,y,z: (x+y)*z)


"""
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 LOAD_FAST                2 (z)
              8 BINARY_MULTIPLY
             10 RETURN_VALUE
"""
