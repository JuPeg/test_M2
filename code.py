from Bio import SeqIO
count = 0
# iterating through all sequences in fasta file
for seq in SeqIO.parse("sequences.fasta","fasta"):
	count = count + 1 # number of sequences
	print(seq.id +" \t  "+ str(len(seq))) # sequences names and lengths
print("\nThere are "+str(count)+" sequences")

