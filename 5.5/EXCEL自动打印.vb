Sub autoprint()


    For i = 1 To 9
    Range("C3").Select
    ActiveCell.FormulaR1C1 = Sheets("A").Range("A" & i).Value
    ActiveWindow.SelectedSheets.PrintOut Copies:=1, Collate:=True, _
        IgnorePrintAreas:=False
    Next
End Sub


