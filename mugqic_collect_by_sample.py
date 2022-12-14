import sys
import csv
import os
import re 

#Argument 1 is the path to the opt_MUGQIC output file
#Argument 2 is the output directory
#This script will output variants present by patient/sample

print("Finished BCFTools filtering. Beginning grouping by patient.")

#Alter this list to include any files that do not follow the typical PAXXXXX naminng format
nonStandardSampleNames = ["2-2419861", "2-2419864", "N2824", "N3873", "S1223", "S1274", "S2417", "S2557", "S585", "S664"] 

samples = dict()

with open(sys.argv[1]) as variants_tsv: 
    variants = csv.reader(variants_tsv, delimiter="\t")

    #Loop through lines, ignoring empty rows

    for line in variants: 
            if len(line) == 0: 
                continue
            else: 

                #Annotate data with ClinVar variant information
                #Add files to samples dict if not already in dict, and add data
                #Dont add file to samples dict if it's already in there, but add any relevant data

                variantDetails = line[-6:]
                command = "esearch -db clinvar -query \"(" + str(variantDetails[1]) + " [Base Position]) AND " + str(variantDetails[0][-2:]) + " [Chromosome]\" | efetch -format docsum | xtract -pattern DocumentSummary -sep \",\" -element title clinical_significance/description"
                clinVarData = re.split('\t|\n', os.popen(command).read())
                if "Pathogenic" in clinVarData: 
                    variantDetails.append("\t" + str(clinVarData))
                else: 
                    variantDetails.append(clinVarData)

                for element in line: 
                    if element not in samples.keys() and (element.startswith("PA") or element in nonStandardSampleNames): 
                        fileName = os.path.join(sys.argv[2], element + ".tsv")
                        samples[element] = fileName
                        newFile = open(fileName, "x")
                        for characteristic in variantDetails: 
                            newFile.write(str(characteristic) + "\t")
                        newFile.write("\n")
                        newFile.close()
                    elif element in samples.keys() and (element.startswith("PA") or element in nonStandardSampleNames): 
                        fileName = samples.get(element)
                        newFile = open(fileName, "a")
                        for characteristic in variantDetails: 
                            newFile.write(str(characteristic) + "\t")
                        newFile.write("\n")
                        newFile.close()
                        

                    
