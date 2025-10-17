# This program finds genes in the genome string
def valid_gene(gene):  # Define function for valid genome
    valid_list = ['A', 'C', 'G', 'T']
    gene_list = list(gene)
    for gen in range(len(gene_list)):
        if gene_list[gen] not in valid_list:
            return False
    return True


def len_of_string(gene):  # Define function for valid length
    gene_list = list(gene)
    if len(gene_list) % 3 != 0:
        return False
    return True


def separated_gene(gene):  # Define function to find genes
    gene_list = list(gene)
    end_gene = ['ATG', 'TAG', 'TAA', 'TGA']
    gene_string = ''.join(gene_list)
    # Find value 'ATG'
    start_gene = gene_string.find('ATG')
    # Use loop to indicate value in the list of gene
    while start_gene != -1:  # The loop ends when reaching index -1
        # Indicate value after 'ATG'
        start_list = gene[start_gene+3:]
        for end in range(0, len(start_list), 3):
            # Display all the values after 'ATG'
            end_list = start_list[end:end+3]
            # Until reaching the value being in the end_list
            if end_list in end_gene:
                break

            print(end_list, end=" ")

        # Continue to find the value 'ATG'
        start_gene = gene.find('ATG', start_gene+1)


def main():  # Define main function
    print("Genes in Genome String")
    gene = str(input('Enter a Genome String: '))
    if valid_gene(gene) is False:
        print("Error: The Genome String is Invalid. Please proceed snd try again")
    elif len_of_string(gene) is False:
        print("Error: The Genome String must have the length be divisible by 3. "
              "Please proceed snd try again")
    else:
        print("Gene Found:", end=" ")
        separated_gene(gene)
        # If after Gene Found returns no value, it means no gene is found in the genome


# Display the result
main()
