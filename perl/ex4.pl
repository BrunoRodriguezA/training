use strict;

#4.1 

my @a = qw(a b c d e);  # quote words - ya no hace falta poner doble comillas 

# print "@a\n";
# print @a, "\n";
# print join("-", @a), "\n";


# 4.2 
my @nums = (10, 4, 7, 1);
my $suma = 0;
my $maximo = 0; 

for my $i(@nums){
    $suma += $i;

    if($i > $maximo){
        $maximo = $i;
    }
}
print "$suma\n"; 
print "$maximo";