from numpy import array

a = array([[1],[2],[3]])
b = array([4,5,6])

#Matrix BroadCasting!!!!!
print( a + b )
#array([[5,6,7],[6,7,8],[7,8,9]])
print( a * b )
#array([[4,5,6],[8,10,12],[12,15,18]])

#a = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
#b = [[4, 4, 4], [5, 5, 5], [6, 6, 6]]
#으로 확장되서 계산된다!!
