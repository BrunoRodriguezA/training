

my @identificador = ('uid', 'samaccount', 'cn');

my $is_unlocked = 0; # false 
my $dn = 'uid';

# foreach my $id(@identificador){

#     if ($is_unlocked == 0) {
#         print "unlocking ..";
#         print "unlocked";
#         $is_unlocked = 1
#     }
# }
# print $is_unlocked


sub saludar{
    my ($nombre, $apellido) = @_;
    return "Hola $nombre $apellido";
}


print saludar("Mundo", "Cruel");


# por cada identificador 
    # ldapserach por identificador 
        # si es 1 
            # desbloquea
            # message desbloqueo OK
            # corta bucle 
        # si es >1 
            # message error duplicado 
            # corta bucle 
        # si es 0
            # message error not found 
            # corta bucle 
# retorn message 
