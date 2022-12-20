# Import the necessary modules
import tkinter as tk
import csv

# Define a function that will compare the two CSV files
# and return a list of differences
def compare_csv_files(file1, file2):
    # Open the first CSV file and read its lines
    with open(file1, 'r') as csvfile1:
        lines1 = csvfile1.readlines()
    
    # Open the second CSV file and read its lines
    with open(file2, 'r') as csvfile2:
        lines2 = csvfile2.readlines()
    
    # Compare the lines in the two files and store the differences
    # in a list
    differences = []
    for i in range(min(len(lines1), len(lines2))):
        if lines1[i] != lines2[i]:
            differences.append((i+1, lines1[i], lines2[i]))
    
    # Return the list of differences
    return differences

# Create the GUI window
root = tk.Tk()
root.title('CSV File Comparison')

# Create a label for the first file
label1 = tk.Label(root, text='First CSV File:')
label1.pack(side=tk.TOP)

# Create an entry for the first file
entry1 = tk.Entry(root)
entry1.pack(side=tk.TOP)

# Create a label for the second file
label2 = tk.Label(root, text='Second CSV File:')
label2.pack(side=tk.TOP)

# Create an entry for the second file
entry2 = tk.Entry(root)
entry2.pack(side=tk.TOP)

# Create a button to compare the files
button = tk.Button(root, text='Compare Files', command=compare_files)
button.pack(side=tk.TOP)

# Create a text widget to display the results
text = tk.Text(root)
text.pack(side=tk.TOP)

# Define the function that will be called when the button is clicked
def compare_files():
    # Get the file names from the entries
    file1 = entry1.get()
    file2 = entry2.get()
    
    # Compare the files and get the list of differences
    differences = compare_csv_files(file1, file2)
    
    # Clear the text widget
    text.delete('1.0', tk.END)
    
    # Display the differences in the text widget
    for diff in differences:
        text.insert(tk.END, 'Line {}:\n'.format(diff[0]))
        text.insert(tk.END, '    File 1: {}'.format(diff[1]))
        text.insert(tk.END, '    File 2: {}\n'.format(diff[2]))

# Start the GUI event loop
root.mainloop()
