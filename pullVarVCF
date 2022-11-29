#!/bin/bash

#This script acts as a parser for the pullVarVCF scripts 
#The subsequently called script will use bcftools to filter VCF's created via either the SV or MUGQIC options on the GenPipes DNAseq pipeline from C3G

#Options passable are: 
#   - s (for SV) *or* -m (for MUGQIC)  
#Both options take four arguments bound by commas (i.e. 17,43044295,43125364,BRCA1,your/path/here). Arguments passed must be: 
#   chromosome (int)
#   start coordinate (int) - as per hg38
#   end coordinmate (int) - as per hg38
#   user supplied identifier for the output directory (for example the gene name for the region of interest) (string)
#   path to the directory containing all data (i.e. a "root" directory under which all data files exist (for -s), or a path to a file containing the data (for -m))
#Add -c *first* for use in Compute Canda clusters (this will load the necessary modules)

while getopts 'cs:m:h' opt; do
  case "$opt" in
    c)
      echo "Loading modules for CC cluster (bcftools and tabix)"
      ./load_modules
      ;;

    s)
      arg="$OPTARG"
      echo "Running SV output analysis"
      set -f
      IFS=,
      array=($OPTARG)
      ./opt_SV ${array[0]} ${array[1]} ${array[2]} ${array[3]} ${array[4]}
      ;;

    m)
      arg="$OPTARG"
      echo "Running MUGQIC output analysis"
      set -f
      IFS=,
      array=($OPTARG)
      ./opt_MUGQIC ${array[0]} ${array[1]} ${array[2]} ${array[3]} ${array[4]}
      ;;

    h)
      echo "Usage: $(basename $0) [-c] ([-s INT,INT,INT,STRING,STRING] or [-m INT,INT,INT,STRING,STRING])"
      exit 0
      ;;

    :)
      echo -e "option requires an argument.\nUsage: $(basename $0) [-c] ([-s INT,INT,INT,STRING,STRING] or [-m INT,INT,INT,STRING,STRING])"
      exit 1
      ;;

    ?)
      echo -e "Invalid command option.\nUsage: $(basename $0) [-c] ([-s INT,INT,INT,STRING,STRING] or [-m INT,INT,INT,STRING,STRING])"
      exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"






