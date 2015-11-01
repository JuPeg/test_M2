from Bio import SeqIO
count = 0

f = open("results.txt","w") # open "results" file

# iterating through all sequences in fasta file
for seq in SeqIO.parse("sequences.fasta","fasta"):
	count = count + 1 # number of sequences
	f.write(seq.id +" \t  "+ str(len(seq)) + "\n") # sequences names and lengths
f.write("\nThere are "+str(count)+" sequences")

f.close() # close results file
