#Media de um aluno FIAP
#Variaveis 
#Nota do semestre 1
cp1 = 7
cp2 = 8
cp3 = 5
gs1 = 6
mediacp1 = (cp1 + cp2 + cp3)/3

#Nota do semestre 2
cp4 = 6
cp5 = 8
cp6 = 9
gs2 = 10
mediacp2 = (cp4 + cp5 + cp6)/3

#Calc de media
media1 = mediacp1*0.4 + gs1*0.6
print('O aluno obteve media' + str(media1) + "no primeiro semestre.')

media2 = mediacp2*0.4 + gs2*0.6
print('O aluno obteve media' + str(media2) + "no segundo semestre.')

#Media final
mediafinal = media1*0.4 + media2*0.6
print('A media final do aluno foi: ' + str(mediafinal))



