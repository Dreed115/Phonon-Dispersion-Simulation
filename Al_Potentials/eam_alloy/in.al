package omp 4

# INITIALIZATION
dimension 3 
boundary p p p
units metal
atom_style atomic 
atom_modify map array

# geometry
read_data	dataAl.pos

# DEFINE INTERATOMIC POTENTIAL
pair_style eam/alloy
pair_coeff * * Al2009.eam.alloy Al
neighbor 2.0 bin 
neigh_modify delay 10 check yes 

#Langevin random seed
variable r equal 57085
variable t equal 300
variable d equal 1

# initialize
velocity all create $t 28459 rot yes dist gaussian mom yes
reset_timestep 0

# fixes 
fix      1 all npt temp $t $t $d iso 1. 1. 1. pchain 8 drag 1.0
fix      2 all phonon 10 50000 500000 map.in AlPhonon

#
timestep 2e-3

# output
#                    1    2    3  4  5     6   7  8  9  10 11 12
thermo_style  custom step temp pe ke press vol lx ly lz xy xz yz
thermo  100

restart 2000000 restart.one restart.two

dump    	3 all atom 50000 dump_LJ_ANA.lammpstrj 

# execution
run 	 3000000
write_restart Restart.final