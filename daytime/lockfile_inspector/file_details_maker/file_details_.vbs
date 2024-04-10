Dim fso, folder, files, root_path, file_output_location, output_filename, file_info, file_path, file_name, file_extension, file_stats, file_modified_time, i, objExcel, objWorksheet

root_path = "C:\gis_local\arcgispro_bits"
file_output_location = "C:\gis_local\arcgispro_bits"
output_filename = "Output_Filename.xlsx"

Set fso = CreateObject("Scripting.FileSystemObject")
Set folder = fso.GetFolder(root_path)
Set files = folder.Files

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = False
Set objWorkbook = objExcel.Workbooks.Add()
Set objWorksheet = objWorkbook.Worksheets(1)

objWorksheet.Cells(1, 1).Value = "File Name"
objWorksheet.Cells(1, 2).Value = "File Path"
objWorksheet.Cells(1, 3).Value = "File Type"
objWorksheet.Cells(1, 4).Value = "Last Modified Time"

i = 2
For Each file In files
    file_path = file.Path
    file_name = fso.GetBaseName(file_path)
    file_extension = fso.GetExtensionName(file_path)
    file_stats = fso.GetFile(file_path)
    file_modified_time = file_stats.DateLastModified
    objWorksheet.Cells(i, 1).Value = file_name
    objWorksheet.Cells(i, 2).Value = file_path
    objWorksheet.Cells(i, 3).Value = file_extension
    objWorksheet.Cells(i, 4).Value = file_modified_time
    i = i + 1
Next

objWorkbook.SaveAs file_output_location & "\" & output_filename
objWorkbook.Close
objExcel.Quit
