use strict;

# 8.1   # devuelve 1 si role eq "admin", si no 0

sub is_admin{
    my ($role) = @_;

    return $role eq "admin"? 1: 0;
}

# print is_admin("admin");

# 8.2   # colapsa espacios múltiples a uno y recorta espacios al inicio/fin
  # devuelve el string normalizado

sub normalize_spaces{
    my ($text) = @_;
    $text =~ s/\s+/ /g;
    $text =~ s/^\s+|\s+$//g;
    return $text;
}

# print normalize_spaces("   holaa   a   ");

# 8.3   # recibe "user=ana id=10 role=admin"
  # devuelve un hash con esas claves/valores
sub parse_kv{
    my ($line) = @_;
    my %h;

    if ($line =~ /user=(\w+)\s+id=(\d+)\s+role=(\w+)/){
        $h{user} = $1;
        $h{id} = $2;
        $h{role} = $3;
    }
    return %h;
}

my %x = parse_kv("user=ana id=10 role=admin");
print %x
# print ref(\@a) <- por printa scalar ? 

