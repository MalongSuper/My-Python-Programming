# Huffman Coding with Heaps
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char  # Character for Huffman encoding
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child
        self.right = None  # Right child

    def __lt__(self, other):
        return self.freq < other.freq


class MaxHeap:
    def __init__(self, maxsize=100):
        self.maxsize = maxsize
        self.heap = [0] * self.maxsize
        self.last = -1
        self.peak = 0

    @staticmethod
    def parent(pos):
        return (pos - 1) // 2

    @staticmethod
    def left_child(pos):
        return 2 * pos + 1

    @staticmethod
    def right_child(pos):
        return 2 * pos + 2

    def is_leaf(self, pos):
        return self.left_child(pos) > self.last

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def insert(self, value):
        if self.last >= self.maxsize:
            print("Overflow")
            return
        self.last += 1
        self.heap[self.last] = value
        current = self.last
        while (self.parent(current) >= 0 and
               self.heap[current] > self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def display(self):
        for i in range(self.last + 1):
            print(f'{self.heap[i].char}: {self.heap[i].freq}', end=" | ")
        print()

    def get_peak(self):
        if self.last >= 0:
            return self.heap[self.peak]

    def max_heapify(self, pos):
        if not self.is_leaf(pos):
            if (self.heap[pos] < self.heap[self.left_child(pos)] or
                    self.heap[pos] < self.heap[self.right_child(pos)]):
                if self.heap[self.left_child(pos)] > self.heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

    def min_heapify(self, pos):
        if not self.is_leaf(pos):
            if ((self.heap[pos] > self.heap[self.left_child(pos)]) or
                    (self.right_child(pos) <= self.last
                     and self.heap[pos] > self.heap[self.right_child(pos)])):
                if (self.right_child(pos) <= self.last
                        and self.heap[self.right_child(pos)] < self.heap[self.left_child(pos)]):
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))
                else:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))

    def delete(self):
        size = self.last + 1
        if size <= 0:
            print("Empty Heap")
            return None
        self.heap[self.peak] = self.heap[self.last]
        self.last -= 1
        self.max_heapify(self.peak)

    def convert_min_heap(self):
        last_node = (self.last - 1) // 2
        for i in range(last_node, -1, -1):
            self.min_heapify(i)


# Function to build the Huffman Tree based on the character frequencies
def build_huffman_tree(frequency):
    heap = MaxHeap(len(frequency))  # Create a max-heap to store nodes
    # Insert all characters and their frequencies as nodes into the heap
    for char, freq in frequency.items():
        heap.insert(Node(char, freq))
    # Convert the heap into a Min-Heap to allow for
    # correct extraction of minimum frequency nodes
    heap.convert_min_heap()
    # Build the Huffman tree by merging nodes with the smallest frequencies
    while heap.last > 0:
        left = heap.get_peak()
        heap.delete()
        right = heap.get_peak()
        heap.delete()
        # Create a new merged node that combines the frequencies of
        # the left and right nodes
        merged = Node(freq=left.freq + right.freq)
        merged.left = left  # The left child of the merged node
        merged.right = right  # The right child of the merged node
        # Insert the merged node back into the heap
        heap.insert(merged)
        # Convert the heap back to Min-Heap after inserting the merged node
        heap.convert_min_heap()
    # Return the root of the Huffman tree (the last remaining node in the heap)
    return heap.get_peak()


# Function to generate Huffman codes by recursively traversing the Huffman tree
def generate_codes(node, prefix, codebook):
    if node is None:
        return
    # If the node represents a character, assign the current prefix as its Huffman code
    if node.char is not None:
        codebook[node.char] = prefix
    # Recursively generate codes for the left and right subtrees
    # Left child: append '0' to prefix; Right child: append '1' to prefix
    generate_codes(node.left, prefix + "0", codebook)
    generate_codes(node.right, prefix + "1", codebook)


# Function to decode an encoded message using the Huffman codebook
def decode_message(encoded_message, codebook):
    # Reverse the codebook to allow for decoding (code -> character mapping)
    reverse_codebook = {v: k for k, v in codebook.items()}
    current_code = ""
    decoded_message = ""
    # Traverse through each bit in the encoded message
    for bit in encoded_message:
        current_code += bit  # Append the bit to the current code
        # If the current code matches a Huffman code in the reverse codebook
        if current_code in reverse_codebook:
            decoded_message += reverse_codebook[current_code]  # Add the corresponding character
            current_code = ""   # Reset the current code to start matching the next character
    return decoded_message  # Return the fully decoded message


def main():
    # Take user's input
    user_input = str(input("Enter a string: "))
    frequency = {}  # The dictionary to store the frequency
    for char in user_input:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    # Step 1: Build the Huffman tree using the frequency table
    root = build_huffman_tree(frequency)
    # Step 2: Generate Huffman codes by recursively traversing the tree
    codebook = {}
    generate_codes(root, "", codebook)
    print("Huffman Codes:")
    for char, code in codebook.items():
        print(f'{char}: {code}')
    # Step 3: Encode the message "Hello" using the generated Huffman codes
    message = user_input
    encoded_message = "".join([codebook[char] for char in message])
    print(f"Encoded Message: {encoded_message}")
    # Step 4: Decode the encoded message using the codebook
    decoded_message = decode_message(encoded_message, codebook)
    print(f"Decoded Message: {decoded_message}")


main()
