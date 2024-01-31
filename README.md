# N-ary Tree Creation and Traversal

This Python program allows you to create an N-ary tree from a given input serialization and perform a postorder traversal of the tree to get the desired traversal output.

## Prerequisites

- Python 3.x installed on your computer.

## Getting Started

1. Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/imro16/Tree-Creation-and-Traversal.git
Navigate to the project directory:
Run Below command
```bash
    cd Tree-Creation-and-Traversal
    # No external dependencies required
    python main.py

Input Serialization
You can customize the input serialization by modifying the input list in the main.py file. Make sure to follow the format mentioned in the code comments.

Viewing the Output
The program will display the postorder traversal of the N-ary tree based on your input serialization.

Example
Here's an example of how to use the program with custom input:

Modify the input list in main.py with your desired input serialization.

Run the program:

```bash
   python main.py
The program will display the postorder traversal result.
# Example usage
input1 = [1, None, 3, 2, 4, None, 5, 6]
tree1 = Solution.createTree(input1)
output1 = Solution.traverseTree(tree1)
print(output1)  # Output: [5, 6, 3, 2, 4, 1]

input2 = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11,
          None, 12, None, 13, None, None, 14]
tree2 = Solution.createTree(input2)
output2 = Solution.traverseTree(tree2)
print(output2)  # Output: [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
