import files.convert_to_lower_case
import files.fs2_replace_xref
import files.fs2_replace_vector3
import files.fs2_replace_lines

import glob
for filename in glob.glob('/ad/file/path/*.toc'):

    files.convert_to_lower_case.convert_to_lower_case(filename)
    files.fs2_replace_xref.fs2_xref_elements(filename)
    files.fs2_replace_vector3.fs2_vector3(filename)
    files.fs2_replace_lines.xref_flow32_direction(filename)
