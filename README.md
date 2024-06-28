# Connected Sinks in a Pipe System

## Overview

This program analyzes a pipe system represented by a 2D rectangular grid of cells. Each cell can contain a source, a sink, or a pipe. The program determines which sinks are connected to the source through valid pipe connections and returns a sorted list of these connected sinks.

## Grid Representation

The grid contains three types of objects:

1. **Source**: Represented by the asterisk character `'*'`. There is exactly one source in the system.
2. **Sinks**: Represented by uppercase letters (`'A'`, `'B'`, `'C'`, etc.). There can be multiple sinks in the system.
3. **Pipes**: Represented by the following characters: `═`, `║`, `╔`, `╗`, `╚`, `╝`, `╠`, `╣`, `╦`, `╩`. Each pipe has openings on 2 or 3 sides of its cell.

Adjacent cells are considered connected if both cells have a pipe opening at their shared edge.

### Examples

- Cells `'╩'` and `'╦'` are connected through their shared edge.
- Cells `'╩'` and `'╔'` are not directly connected through their shared edge, but they may be connected through other cells.

The source and sinks are treated as having pipe openings on all their edges. For example, the cells `'A'` and `'╦'` are connected through their shared edge, but the cells `'B'` and `'╔'` are not directly connected.

## Input File Format

The input file specifies the location of objects in the grid. Each row contains:
- The character representing the object (`'*'`, an uppercase letter, or a pipe).
- The x-coordinate of the object in the grid.
- The y-coordinate of the object in the grid.

Coordinates have a minimum value of 0.

### Example Input File

The following example represents a pipe system:
```
* ╣   ╔ ═ A
  ╠ ═ ╝    
  C   ╚ ═ B
```
Below are the contents of an input file that specifies the example pipe system illustrated above. The order of the rows within the file is arbitrary, so the rows could be given in any order.
```
* 0 2
C 1 0
╠ 1 1
╣ 1 2
═ 2 1
╚ 3 0
╝ 3 1
╔ 3 2
═ 4 0
═ 4 2
B 5 0
A 5 2
```

## Functionality

The function `connected_sinks(file_path)` takes a single argument, which is the file path of the input text file. It returns a string of uppercase letters representing the sinks connected to the source, in alphabetical order.

### Algorithm

1. **Read Input File**: Parse the input file to create a grid representation.
2. **Initialize BFS**: Use a breadth-first search (BFS) algorithm starting from the source to explore all valid connections.
3. **Check Connections**: Determine if two cells are connected based on their pipe types and positions.
4. **Collect Connected Sinks**: Identify and collect all sinks connected to the source.
5. **Return Result**: Return the sorted list of connected sinks as a string.

## Usage

To use the program, place your input data in a text file and call the function with the file path. For example:

```python
result = connected_sinks('input_file.txt')
print("Connected Sinks:", result)
```
