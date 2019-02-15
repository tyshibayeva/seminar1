from myclass import Car # import klassa

car1 = Car()   #sozdanie obekt car1 iz classa Car
car1.disp_inf() #vivodim informaciyy(znacheniya atribut)


types = "sedan" #sozdaem peremennu types so znach="sedan"
label = "nissan"
color = "red"
car1.change_inf(types, label,color) #novaya funkciya izmenyauchaya znacheniya tekuchih atributov na novie
car1.disp_inf() #vivodim informaciyy(znacheniya atribut)


 
