use strict;
my %h = (host => "db1", port => 5432, env => "prod");

# 5.1 
#print "host=$h{host} port=$h{port} env=$h{env}";
# if (exists $h{key})

# 5.2 
# if ($h{env} eq "prod"){
#     $h{env} = "pre";
#     $h{retries} = 3;
# }
# # 5.3 
# for my $key (keys %h){
#     print "$key=$h{$key}\n";
# }

# 5.4 

my $text = "hola hola mundo mundo mundo";
my @list = split(" ", $text);
my %count;

for my $ch (@list){
    if (exists $count{$ch}){
        $count{$ch} +=1;
    }
    else{
        $count{$ch} = 1;
    }
}

for my $word (sort keys %count) {
    print "$word => $count{$word}\n";
}