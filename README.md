# PDF-Merger
 python program to merge pdf files into one file

so I was going to combine 10 flowcharts which where odf files into one file and I thought it would be cool to have a program to do that!
So I wrote it :D


Merge a list of PDF files and save the combined result into the 'output_file'.
'page_range' to select a range of pages (behaving like Python's range() function) from the input files
    e.g (0,2) -> First 2 pages 
    e.g (0,6,2) -> pages 1,3,5
bookmark -> add bookmarks to the output file to navigate directly to the input file section within the output file.