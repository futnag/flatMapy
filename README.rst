flatMapy
========================

PythonでScalaのflatmapやflattenを使えるようになります。
flat_allは深くネストしたリストをすべて平坦化します。


INSTALLATION
==============
cloneして、ディレクトリ内にて
::

 $ python setup.py install






USAGE
============

.. code:: python

  import flatMapy
   
  flatMapy.flatmap(str, [[1,2,3], [4,5,6]])
  # ['1','2','3','4','5','6']
  
  flatMapy.flatten([[1,2,3], [4,5,6]])
  # [1,2,3,4,5,6]
  
  flatMapy.flatten([[1,2,3], [4,[5,6]]])
  # [1,2,3,4,[5,6]]
  
  flatMapy.flat_all([2,4,5, (3,4,5), [3,4,(5,56,(3,4))], (4,50)])
  # [2, 4, 5, 3, 4, 5, 3, 4, 5, 56, 3, 4, 4, 50]
  
  flatMapy.flat_all(((1,2,3), (4,5,6)))
  # (1,2,3,4,5,6)
  
  flatMapy.flat_all(((1,2,(3)), (4,(5,6))))
  # (1,2,3,4,5,6)
  
  flatMapy.flatten(['hello', 'world'])
  #['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
  
  flatMapy.flatmap(lambda x: x.upper(), ['hello', 'world'])
  # ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']

  flatMapy.flatten([['hello'], 'world'])
  # ['hello', 'w', 'o', 'r', 'l', 'd']

  flatMapy.flat_all([['hello'], 'world'])
  # ['hello', 'world']
