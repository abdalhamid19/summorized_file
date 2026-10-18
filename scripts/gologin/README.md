# GoLogin UI helpers

`Start-Gologin.ps1` starts GoLogin if its main window is absent. Its success means a window was found; it does not claim that the page finished loading or that sign-in succeeded.

`Inspect-GologinUI.ps1` reads the visible Windows UI Automation tree for the open GoLogin window. It does not click controls, enter data, save screenshots, or read values from edit and password fields. Email-like text is redacted in its output.

`gologin_uia.py` inspects GoLogin through `pywinauto` and provides narrow actions: open the account menu, choose the exact `Logout` option, and open the sign-up form. The sign-up command only opens the form; it does not enter data, create an account, submit registration, or accept terms. Inspection omits values from edit, combo, document, and password controls, and redacts email-like text and long numbers. The sign-out action reports success only after the login screen is visible.

## Run

```powershell
powershell -ExecutionPolicy Bypass -File .\Start-Gologin.ps1
powershell -ExecutionPolicy Bypass -File .\Inspect-GologinUI.ps1
.\.venv\Scripts\python.exe -X utf8 .\gologin_uia.py inspect
.\.venv\Scripts\python.exe -X utf8 .\gologin_uia.py open-account-menu
.\.venv\Scripts\python.exe -X utf8 .\gologin_uia.py sign-out
.\.venv\Scripts\python.exe -X utf8 .\gologin_uia.py open-sign-up
```

Run the commands from this directory. The Python environment is isolated in `.venv` and contains `pywinauto==0.6.9`. `-X utf8` keeps non-ASCII UI text from failing on Windows console encodings. The scripts use the current Windows user and do not store credentials, temporary email addresses, or verification codes.

## Current observed state

GoLogin v4.11.3 is signed out with the `Create Account` form open. The account menu was opened and `Logout` was selected by the script; the login page was then verified in the UI Automation tree. The reusable `open-sign-up` action opened the form and verified its title. A checkout dialog for an annual Enterprise plan appeared earlier and was closed with its X only; no payment was made. No account data, password, terms acceptance, or verification code has been submitted.
