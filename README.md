# fs2-tofs4-xref-file-converter
This project is a short program, which converts the xref-files from the Aerofly-fs2 format to the fs4 format.

In the folder "fs2_to_fs4_converter" is the main.py file, which will be executed via Terminal.
There is also the "fs2_xref_flow32_direction.txt" and the "fs4_xref_flow64.txt" file, the programm will look for those files (and replace them).
It will also convert the entire xref-file to lowercase and it willreplace [xref] and [vector3_float64] with [tm_airport_pd_xref] and [vector2_float64].

  step by step
1.download the entire "fs2_to_fs4_convertr" folder
2.open the main.py file and adyour path to the foldde, which contains the xref-file (important: onlyone file at time)
3.open Terminal
4.cd /path/to/main.py
5.python3 main.py

If you have done everythink correct your file will be convertet as wanted.

This converter only works with .txt and .toc -files.
It is designd and tested for MacOS 11.0. or higher.
