lado = input("Informe a medida do lado da sala: ");

if ~(lado < 0) then
    area = lado * lado;
    printf("A area da sala é de f%", area)
else
    printf("O valor digitado é invalido.");
end

/*-------------------------------------------*/

total = 0
x = input('Digite o primeiro número: ');
while (x ~= 0)
    total = total + x;
    x = input('Digite mais um valor ou Zero para terminar a soma: ');
end
printf('A soma dos números informados é: %d', total);