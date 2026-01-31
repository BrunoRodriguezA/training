use strict;
use warnings; 

# 2.1 
my $n = -1 ; 

if ($n > 0){
    print "positivo"
}
elsif($n == 0){
    print "cero"
}
else{
    print "negativo"
}

print "\n";

# 2.2 

my $user = "ana";
my $role = "viewer";
# print $role eq "admin"? "ok\n": "denied\n";
$role = "admin";
# print $role eq "admin"? "ok\n": "denied\n";

# 2.3 

# my $s = "  hola  ";
my $s = "hola";
# print $s;
if ($s =~ /^\s+|\s+$/){
    print "tiene espacios";
}else{
    # $s =~ s/\s+//g;
    print "limpio"
}