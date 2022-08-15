#!/bin/bash -e
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --partition=batch
#SBATCH --constraint="intel"
#SBATCH -J compress
#SBATCH -o std.out
#SBATCH -e std.err
#SBATCH --time=2:00:00
#SBATCH --mail-user=arun.jangir@kaust.edu.sa
#SBATCH --mail-type=ALL

# loading modules:
./compress.sh
