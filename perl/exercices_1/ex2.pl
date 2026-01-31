local $" = ","; 

my @x = (1,2,3);
print @x, "\n"; # pega elementos sin separador 
print "@x\n"; # interpola con $" == " " por defecto 
print join("-", @x), "\n"; # join que junta con el char - como separador 

# print join(",", @x), "\n";