my @letras = qw(a b c d e f);
my @sel = @letras[0,2,5];
print "@sel\n"; 

my @dest;
@dest[0,1,2] = @letras[3,4,5];
# print "@dest\n";
print join(" ", @dest), "\n"; 