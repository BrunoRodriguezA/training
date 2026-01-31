use strict;

my %h = (host => "db1", port => 5432, env => "prod");

print "host=$h{host}, port=$h{port}\n"; 

foreach my $key (keys %h){
    print "$h{$key}\n";
}