use strict;
#3.1 
my $cont = 1;

# while ($cont <= 10){
#     print "$cont\n";
#     $cont++;
# }

# 3.2 
# for (my $i=2; $i <= 20; $i++ ){
# # for $n (2..20){
#     if ($i % 2 == 0){
#         print "$i\n"
#     }
# }

# 3.3 

# my @nums = (3,5,7,9);

# for $n (@nums){
#     print $n ** 2,"\n";
# }



# 3.4 
for my $i (1..30){
    if($i % 3 == 0){
        next;
    }
    print "$i\n"
}