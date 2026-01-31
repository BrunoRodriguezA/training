#! /usr/bin/perl
use strict;
#use warnings;

# VARIABLES ESCLAR, ARRAY, DICT 
my $age  = 22;
my $name = "Pep";
my $salary = "130";

# ARRAYS 
my @names = ("Pep", "Maria", "Ema");
my @ages = (25,28,31);

print "Age = $age\n";
print "Name = $name\n";
print "salary = $salary\n";

print "\$ages[0] = $ages[0]\n";
print "\$ages[1] = $ages[1]\n";
print "\$names[0] = $names[0]\n";
print "\$names[1] = $names[1]\n"; 

# DICT 
my %data = ('Danish', 12, 'Raju', 40, 'Pipi', 25);

print "\$data{'Danish'} = $data{'Danish'}\n";
print "\$data{'Pipi} = $data{'Pipi'}\n"; 

# CONCATENATE 
my $mix = $name .' ' . $age; 
print "$mix\n";

# MULTIPLICAR 
my $stringvar = "abc";  # si no tiene parte numerica Perl lo toma como 0 
print ($stringvar * 2); 

# INCREMENTAR 
my $x = "xyz"; $x++;
my $y = "b9"; $y++; 
my $z = "99"; $z++;
my $w = "z"; $w++; # Ultima pos A y incrementa pos = AA 
my $p = "a-b"; $p++;  # el signo - impide que perl lo trate como string, pasa a 0 

print "$x\n";
print "$y\n";
print "$z\n";
print "$w\n";
print "$p\n";

# REPETIR 
print "-" x 10;
print "\n";
print "ab" x 3 ; 
print "\n";
my @pat = (1,2) x 3; 
print "@pat\n";

my $dec = "1.2p34"; $dec++;
print "$dec\n";
