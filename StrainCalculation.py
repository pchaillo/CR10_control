import CR10_Duino as CR10_test
printer = CR10_test.SerialDuino() 
[x,y,z]=printer.getCurrentPosition()
print(z)
