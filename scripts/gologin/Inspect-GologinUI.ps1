$ErrorActionPreference = 'Stop'

$Executable = Join-Path $env:LOCALAPPDATA 'Programs\Gologin\Gologin.exe'
$Process = Get-Process -Name Gologin -ErrorAction SilentlyContinue |
    Where-Object { $_.Path -eq $Executable -and $_.MainWindowHandle -ne 0 } |
    Select-Object -First 1

if (-not $Process) {
    [Console]::Error.WriteLine('GoLogin main window was not found. Run Start-Gologin.ps1 first.')
    exit 1
}

Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes

$Window = [System.Windows.Automation.AutomationElement]::FromHandle($Process.MainWindowHandle)
if (-not $Window) {
    [Console]::Error.WriteLine('Windows UI Automation could not attach to the GoLogin window.')
    exit 2
}

$Controls = $Window.FindAll(
    [System.Windows.Automation.TreeScope]::Descendants,
    [System.Windows.Automation.Condition]::TrueCondition
)
$Items = @()
$IndexLimit = [Math]::Min($Controls.Count, 1000)

for ($Index = 0; $Index -lt $IndexLimit; $Index++) {
    try {
        $Current = $Controls.Item($Index).Current
        if ($Current.IsOffscreen) {
            continue
        }

        $Type = $Current.ControlType.ProgrammaticName
        $Name = $Current.Name
        if ($Type -match 'Edit|Password|ComboBox') {
            $Name = '[value omitted]'
        } elseif ($Name) {
            $Name = [regex]::Replace(
                $Name,
                '(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',
                '[email redacted]'
            )
        }

        $AutomationId = [regex]::Replace(
            $Current.AutomationId,
            '(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',
            '[email redacted]'
        )

        $Bounds = $Current.BoundingRectangle
        $Items += [pscustomobject]@{
            Index = $Index
            Type = $Type
            Name = $Name
            AutomationId = $AutomationId
            Enabled = $Current.IsEnabled
            Bounds = @{
                X = [Math]::Round($Bounds.X, 1)
                Y = [Math]::Round($Bounds.Y, 1)
                Width = [Math]::Round($Bounds.Width, 1)
                Height = [Math]::Round($Bounds.Height, 1)
            }
        }
    } catch {
        $Items += [pscustomobject]@{
            Index = $Index
            Type = 'unavailable'
            Name = ''
            AutomationId = ''
            Enabled = $false
            Bounds = $null
        }
    }
}

[pscustomobject]@{
    Status = 'tree-read'
    ProcessId = $Process.Id
    WindowTitle = $Process.MainWindowTitle
    ProcessResponding = $Process.Responding
    TotalElements = $Controls.Count
    ReturnedElements = $Items.Count
    Elements = $Items
} | ConvertTo-Json -Depth 5
