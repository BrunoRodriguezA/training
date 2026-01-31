#! /usr/bin/perl
use strict;
use warnings;

my @a = (1,2,3);
my @b = (4,5);
my @c = (@a, @b, 6);

#print "@c\n";

my %h = (key1 => 'a', key2 => 'b');

# print "$h{key1}, $h{key2}";
# print %h

# my @vals = @h{qw(key1 key2)};
# print "@vals\n";

#my @g = qw(uno dos tres); 
#print "@g\n";

# LISTAS 

my @list1 = ("one", "two", "three", "four");
my $elem = $list1[0];
my $last_elem = $list1[-1];

#print "$elem\n";
#print "$last_elem\n";

# SLICING LIST

my @letras = ("a", "b", "c", "d", "e");
#print "@letras\n";

# my @primeras = @letras[0,2,4];
my @primeras;
@primeras[0,1,2] = @letras[0,2,4];
#print "@primeras\n";

# RANGE LIST 
my @list2 = (1..10);
#print "@list2\n";

my @list3 = (2.1..6.3);  # perl no genera rango descimales, solo discretas numeros = entero
# print "@list3\n";
# print @list3;

my ($var1, $var2) = @list3;
# print "$var1, $var2";


# SORTED 

my @numbers = (9,2,5,1,3);
my @names = ('rosy', 'pep', 'angela', 'zoe', 'bruno');

my @sorted_nums = sort @numbers;
my @sorted_names = sort @names;
my @desc_nums = reverse sort @numbers;
my @revers_names = reverse sort @names;


# print "@sorted_nums\n";
# print "@sorted_names\n";
# print "@desc_nums\n";
# print "@revers_names\n";

my $names_2 = join(":", @names);
my $names_3 = join(" ", @names, 'hugo');
print "$names_2\n";
print "$names_3\n";